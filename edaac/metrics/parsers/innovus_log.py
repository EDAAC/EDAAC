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


def _time_string_to_seconds(time):
    hour, minute, second = list(map(float, time.split(':')))
    return int(second + minute*60 + hour*60*60)

def _time_string_to_minutes(time):
    hour, minute, second = list(map(float, time.split(':')))
    return int(second/60.0 + minute + hour*60)

def parse_innovus_log(log_file_path):
    logger = get_logger()
    metrics = {
        'compute_cpu_time_total': None,
        'compute_real_time_total': None,
        'compute_mem_total': None,
        'area_stdcell': None,
        'area_total': None
    }

    try:
        with open(log_file_path, 'r') as f:
            report = ''.join(f.readlines())
    except Exception as e:
        logger.error('Can\'t read report file: %s. Skipping ..',
                     log_file_path)
        return

    # Stats
    regex = '--- Ending \"Innovus\" \(totcpu=(?P<cpu_total>[\-0-9\.:]*), real=(?P<time_total>[\-0-9\.:]*), mem=(?P<mem_total>[\-0-9\.]*)M\) ---'
    m = re.search(regex, report)
    if m:
        metrics['compute_cpu_time_total'] = _time_string_to_seconds(m.group('cpu_total')) 
        metrics['compute_real_time_total'] = _time_string_to_seconds(m.group('time_total'))
        metrics['compute_mem_total'] = float(m.group('mem_total'))
    
    # Area
    regex = ' *= stdcell_area [0-9\.]* sites \((?P<stdcell_area>[0-9\.]*) um\^2\) \/ alloc_area [0-9\.]* sites \((?P<total_area>[0-9\.]*) um\^2\).*'
    m = re.search(regex, report)
    if m:
        metrics['area_stdcell'] = int(float(m.group('stdcell_area')))
        metrics['area_total'] = int(float(m.group('total_area')))

    logger.info('Successfully extracted metrics from %s', log_file_path)

    return metrics
