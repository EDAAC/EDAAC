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

class Technology:
    """
    A class used to represent an Technology used in a Project
    """
    def __init__(foundry=None, process=None, beol=None, track=None, \
        opv=None, vtc=None, config=None, version=None, rag=None):
        # TODO: get technology ID by creating or getting a MongoDB document
        self.id = 1
        self.foundry = foundry
        self.process = process  # e.g. 16nm
        self.beol = beol        # back end of line: label that is given by the foundry; the metal stack
        self.track = track      # the heights of the track
        self.opv = opv          # operating voltage
        self.vtc = vtc          # Vt and channel width
        self.config = config
        self.version = version
        self.rag = rag
        