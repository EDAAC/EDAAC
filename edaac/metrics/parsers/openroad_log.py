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

def parse_openroad_log(log_file_path, tool):
    logger = get_logger()
    if tool == "" or tool is None:
        logger.warning('No tool specified')
        return
    
    if tool.lower() == 'opensta':
        return _parse_opensta_log(log_file_path)


def _parse_opensta_log(log_file_path):
    logger = get_logger()
    
    metrics = {
        'slack__negative__total': None,
        'slack__negative__worst': None,
        'std__area__total': None,
        'util': None
    }

    try:
        with open(log_file_path, 'r') as f:
            report = ''.join(f.readlines())
    except Exception as e:
        logger.error('Can\'t read report file: %s. Skipping ..',
                     log_file_path)
        return

    # slack
    regex = 'tns (?P<tns>[0-9\.]*)\n'
    m = re.findall(regex, report)
    if m:
        metrics['slack__negative__total'] = float(m[-1])
    
    regex = 'wns (?P<wns>[0-9\.]*)\n'
    m = re.findall(regex, report)
    if m:
        metrics['slack__negative__worst'] = float(m[-1])
    
    # area & util
    regex = 'Design area (?P<area>[0-9\.]*) u\^2 (?P<util>[0-9\.]*)\% utilization.'
    m = re.findall(regex, report)
    if m:
        metrics['std__area__total'] = float(m[-1][0])
        metrics['util'] = float(m[-1][1])

    logger.info('Successfully extracted metrics from %s', log_file_path)

    return metrics