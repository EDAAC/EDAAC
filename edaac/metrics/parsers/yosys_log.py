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


def parse_yosys_log(log_file_path):
    logger = get_logger()
    metrics = {
        'run__synth__yosys_version': None,
        'synth__inst__num__total': None,
        'synth__inst__stdcell__area__total': None,
        'synth__wire__num__total': None,
        'synth__wirebits__num__total': None,
        'synth__memory__num__total': None,
        'synth__memorybits__num__total': None,
        'run__synth__warning__total': None,
        'run__synth__warning__unique__total': None,
        'run__synth__cpu__total': None,
        'run__synth__mem__total': None
    }

    try:
        with open(log_file_path, 'r') as f:
            report = ''.join(f.readlines())
    except Exception as e:
        logger.error('Can\'t read report file: %s. Skipping ..',
                     log_file_path)
        return

    # version
    regex = 'Yosys (?P<yosys_version>[0-9]+.*)\n'
    m = re.search(regex, report)
    if m:
        metrics['run__synth__yosys_version'] = m.group('yosys_version')

    # number of cell instances
    regex = '.*Number of cells: *(?P<number_of_cells>[0-9]*).*'
    matches = re.findall(regex, report)
    if matches:
        metrics['synth__inst__num__total'] = int(float(matches[-1]))

    # std cell area
    regex = '.*Chip area for module .*\: *(?P<chip_area>[0-9\.]*).*'
    matches = re.findall(regex, report)
    if matches:
        metrics['synth__inst__stdcell__area__total'] = float(matches[-1])
    
    # wires
    regex = '.*Number of wires.*\: *(?P<number_of_wires>[0-9\.]*).*'
    matches = re.findall(regex, report)
    if matches:
        metrics['synth__wire__num__total'] = int(matches[-1])
    regex = '.*Number of wire bits.*\: *(?P<number_of_wire_bits>[0-9\.]*).*'
    matches = re.findall(regex, report)
    if matches:
        metrics['synth__wirebits__num__total'] = int(matches[-1])
    
    # memory
    regex = '.*Number of memories.*\: *(?P<number_of_memory>[0-9\.]*).*'
    matches = re.findall(regex, report)
    if matches:
        metrics['synth__memory__num__total'] = int(matches[-1])
    regex = '.*Number of memory bits.*\: *(?P<number_of_memory_bits>[0-9\.]*).*'
    matches = re.findall(regex, report)
    if matches:
        metrics['synth__memorybits__num__total'] = int(matches[-1])
    
    # warnings
    regex = 'Warnings: (?P<warning_unique>[0-9]*) unique messages, (?P<warning_total>[0-9]*) total'
    m = re.search(regex, report)
    if m:
        metrics['run__synth__warning__total'] = int(m.group('warning_total'))
        metrics['run__synth__warning__unique__total'] = int(m.group('warning_unique'))
    
    # runtime and memory
    regex = '.*CPU\: user (?P<cpu_user_time>[0-9\.]*)s system.*MEM\: (?P<memory>[0-9\.]*) MB peak.*'
    m = re.search(regex, report)
    if m:
        metrics['run__synth__cpu__total'] = float(m.group('cpu_user_time'))
        metrics['run__synth__mem__total'] = float(m.group('memory'))

    logger.info('Successfully extracted metrics from %s', log_file_path)

    return metrics
