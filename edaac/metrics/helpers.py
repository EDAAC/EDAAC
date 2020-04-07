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

from collections import defaultdict
import edaac.metrics.synth as ls
import edaac.metrics.timing as timing

__available_tools__ = defaultdict(lambda: None)
__available_tools__['yosys'] =  {
    'default_version': '0_8_576',
    'versions': {
        '0_8_576': ls.yosys.parse_0_8_567
    }
}
__available_tools__['Tempus'] =  {
    'default_version': '19_10_p002_1',
    'versions': {
        '19_10_p002_1': timing.Tempus.parse_19_10_p002_1
    }
}

def registered_tool(tool_name):
    global __available_tools__
    return __available_tools__[tool_name]


if __name__ == "__main__":
    print(registered_tool('yosys'))
    print(registered_tool('dummy'))