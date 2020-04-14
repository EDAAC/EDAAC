'''
EDA Analytics Central (EDAAC)
Copyright (c) 2019, Abdelrahman Hosny
All rights reserved.

BSD 3-Clause License

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''

import re
from edaac.log import get_logger


def parse_innovus_drc_report(report_file_path):
    logger = get_logger()
    # this could be substituted by a default dictionary
    # but keeping it this way to see what metrics this function reports
    metrics = {
        'drv_total': None,
        'drv_short_metal_total': None,
        'drv_short_metal_area': None,
        'drv_short_cut_total': None,
        'drv_short_cut_area': None,
        'drv_out_of_die_total': None,
        'drv_out_of_die_area': None,
        'drv_spacing_total': None,
        'drv_spacing_parallel_run_length_total': None,
        'drv_spacing_eol_total': None,
        'drv_spacing_cut_total': None,
        'drv_min_area_total': None
    }

    try:
        with open(report_file_path, 'r') as f:
            report = ''.join(f.readlines())
    except Exception as e:
        logger.error('Can\'t read report file: %s. Skipping ..',
                     report_file_path)
        return

    # DRV Total
    regex = 'Total Violations +: +[0-9]+'
    matches = re.findall(regex, report)
    for match in matches:
        metrics['drv_total'] = int(match.split(':')[1].strip())

    # Short Violations
    regex = 'SHORT: \( Metal Short \) +.*\nBounds +: +.*\n'
    matches = re.findall(regex, report)
    metrics['drv_short_metal_total'] = len(matches)
    metrics['drv_short_metal_area'] = 0.0
    for match in matches:
        violation, bounds = match.strip().split('\n')
        m = re.search(
            '\((?P<x1>[\-0-9\. ]*),(?P<y1>[\-0-9\. ]*)\) +\((?P<x2>[\-0-9\. ]*),(?P<y2>[\-0-9\. ]*)\)', bounds)
        x1, x2 = float(m.group('x1').strip()), float(m.group('x2').strip())
        y1, y2 = float(m.group('y1').strip()), float(m.group('y2').strip())
        area = abs(x1 - x2) * abs(y1 - y2)
        metrics['drv_short_metal_area'] += area
    metrics['drv_short_metal_area'] = float(
        format(metrics['drv_short_metal_area'], '.8f'))

    regex = 'SHORT: \( Cut Short \) +.*\nBounds +: +.*\n'
    matches = re.findall(regex, report)
    metrics['drv_short_cut_total'] = len(matches)
    metrics['drv_short_cut_area'] = 0.0
    for match in matches:
        violation, bounds = match.strip().split('\n')
        m = re.search(
            '\((?P<x1>[\-0-9\. ]*),(?P<y1>[\-0-9\. ]*)\) +\((?P<x2>[\-0-9\. ]*),(?P<y2>[\-0-9\. ]*)\)', bounds)
        x1, x2 = float(m.group('x1').strip()), float(m.group('x2').strip())
        y1, y2 = float(m.group('y1').strip()), float(m.group('y2').strip())
        area = abs(x1 - x2) * abs(y1 - y2)
        metrics['drv_short_cut_area'] += area
    metrics['drv_short_cut_area'] = float(
        format(metrics['drv_short_cut_area'], '.8f'))

    # Out of Die Violations
    regex = 'SHORT: \( Out Of Die \) +.*\nBounds +: +.*\n'
    matches = re.findall(regex, report)
    metrics['drv_out_of_die_total'] = len(matches)
    metrics['drv_out_of_die_area'] = 0.0
    for match in matches:
        violation, bounds = match.strip().split('\n')
        m = re.search(
            '\((?P<x1>[\-0-9\. ]*),(?P<y1>[\-0-9\. ]*)\) +\((?P<x2>[\-0-9\. ]*),(?P<y2>[\-0-9\. ]*)\)', bounds)
        x1, x2 = float(m.group('x1').strip()), float(m.group('x2').strip())
        y1, y2 = float(m.group('y1').strip()), float(m.group('y2').strip())
        area = abs(x1 - x2) * abs(y1 - y2)
        metrics['drv_out_of_die_area'] += area
    metrics['drv_out_of_die_area'] = float(
        format(metrics['drv_out_of_die_area'], '.8f'))

    # Spacing Violations
    regex = 'EndOfLine: \( EndOfLine Spacing \) +.*\nBounds +: +.*\n'
    matches = re.findall(regex, report)
    metrics['drv_spacing_eol_total'] = len(matches)

    regex = 'SPACING: \( ParallelRunLength Spacing \) +.*\nBounds +: +.*\n'
    matches = re.findall(regex, report)
    metrics['drv_spacing_parallel_run_length_total'] = len(matches)

    regex = 'CUTSPACING: +.*\nBounds +: +.*\n'
    matches = re.findall(regex, report)
    metrics['drv_spacing_cut_total'] = len(matches)

    metrics['drv_spacing_total'] = metrics['drv_spacing_eol_total'] + \
        metrics['drv_spacing_parallel_run_length_total'] + \
        metrics['drv_spacing_cut_total']

    # Minimum Area Violations
    regex = 'MAR: +\( +Minimum Area +\) +.*\nBounds +: +.*\n'
    matches = re.findall(regex, report)
    metrics['drv_min_area_total'] = len(matches)

    logger.info('Successfully extracted metrics from %s', report_file_path)

    return metrics
