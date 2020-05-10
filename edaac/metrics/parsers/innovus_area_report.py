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

def parse_innovus_area(log_file_path):
    logger = get_logger()
    metrics = {
        'area_stdcell': None,
        'area_stdcell_count': None
    }

    try:
        with open(log_file_path, 'r') as f:
            report = ''.join(f.readlines())
    except Exception as e:
        logger.error('Can\'t read report file: %s. Skipping ..',
                     log_file_path)
        return

    # Area
    regex = '[-]*\n[a-zA-Z\_ ]*(?P<area_stdcell_count>[0-9]+) *(?P<area_stdcell>[0-9\.]+).*'
    m = re.search(regex, report)
    if m:
        metrics['area_stdcell'] = float(m.group('area_stdcell')) 
        metrics['area_stdcell_count'] = int(m.group('area_stdcell_count')) 

    logger.info('Successfully extracted metrics from %s', log_file_path)

    return metrics
