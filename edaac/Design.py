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

class Design:
    """
    A class used to represent an Design used in a Project
    """
    def __init__(name=None, runset_tag=None, runset_id=None, \
        rtl_config=None, rtl_tag=None, rtl_rag=None):
        # TODO: get design ID by creating or getting a MongoDB document
        self.id = 1
        self.name = name

        # Runsets: all RTL related tags for the release candidates
        self.runset_tag = runset_tag
        self.runset_id = runset_id

        # RTL configs
        self.rtl_config = rtl_config
        self.rtl_tag = rtl_tag

        # RAG = Red, Amber, Green.
        # Red -> no much verification ran on it
        # Amber -> alpha or beta release with some levels of verifications on
        # Green -> release candidate
        self.rtl_rag = rtl_rag
