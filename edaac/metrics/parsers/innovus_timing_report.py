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

def parse_innovus_timing_report(report_file_path):
    logger = get_logger()
    metrics = {}

    try:
        with open(report_file_path, 'r') as f:
            lines = f.readlines()
            arrival_time_lines = list(filter(lambda l: '- Arrival Time' in l, lines))
            arrival_time = re.findall(r'-?\d+\.?\d*', arrival_time_lines[0])[0]
            metrics['arrival_time'] = float(arrival_time)
            
            logger.info('Successfully extracted metrics from %s', report_file_path)

    except Exception as e:
        logger.error('Can\'t read report file: %s. Skipping ..', report_file_path)

    return metrics