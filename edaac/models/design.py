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

import mongoengine as mongo


class Design(mongo.EmbeddedDocument):
    """
    A class used to represent a Design used in a Project
    """
    name = mongo.StringField(required=True)
    rtl_files = mongo.ListField(mongo.StringField())
    netlist_file = mongo.StringField()
    sdc_file = mongo.StringField()

    # Runsets: all RTL related tags for the release candidates
    runset_tag = mongo.StringField()
    runset_id = mongo.StringField()

    # RTL configs
    rtl_config = mongo.StringField()
    rtl_tag = mongo.StringField()

    # RAG = Red, Amber, Green.
    # Red -> no much verification ran on it
    # Amber -> alpha or beta release with some levels of verifications on
    # Green -> release candidate
    rtl_rag = mongo.StringField()
