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

from edaac.log import get_logger
import re


def parse_innovus_power_report(report_file_path):
    logger = get_logger()
    # this could be substituted by a default dictionary
    # but keeping it this way to see what metrics this function reports
    metrics = {
            'power_internal_total': None,
            'power_switching_total': None,
            'power_leakage_total': None,
            'power_internal_percentage': None,
            'power_switching_percentage': None,
            'power_leakage_percentage': None,
            'power_total': None,
        }

    try:
        with open(report_file_path, 'r') as f:
            report = ''.join(f.readlines())
    except Exception as e:
        logger.error('Can\'t read report file: %s. Skipping ..',
                     report_file_path)
        return

    # Internal power
    regex = 'Total Internal Power:[ \t]+(?P<total>[0-9\.]*)[ \t]+(?P<percentage>[%0-9\.]*)%'
    m = re.search(regex, report)
    if m:
        metrics['power_internal_total'] = float(m.group('total'))
        metrics['power_internal_percentage'] = float(m.group('percentage'))

    # Switching power
    regex = 'Total Switching Power:[ \t]+(?P<total>[0-9\.]*)[ \t]+(?P<percentage>[%0-9\.]*)%'
    m = re.search(regex, report)
    if m:
        metrics['power_switching_total'] = float(m.group('total'))
        metrics['power_switching_percentage'] = float(m.group('percentage'))
    
    # Leakage power
    regex = 'Total Leakage Power:[ \t]+(?P<total>[0-9\.]*)[ \t]+(?P<percentage>[%0-9\.]*)%'
    m = re.search(regex, report)
    if m:
        metrics['power_leakage_total'] = float(m.group('total'))
        metrics['power_leakage_percentage'] = float(m.group('percentage'))
    
    # Total power
    regex = 'Total Power:[ \t]+(?P<total>[0-9\.]*)'
    m = re.search(regex, report)
    if m:
        metrics['power_total'] = float(m.group('total'))
    
    logger.info('Successfully extracted metrics from %s', report_file_path)

    return metrics
