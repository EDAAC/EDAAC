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
from .Design import Design
from .Technology import Technology
from .Flow import Flow
from .log import get_logger
from .metrics.helpers import registered_tool

class Project(mongo.Document):
    """
    A class used to represent an EDA project
    """
    name = mongo.StringField(required=True, primary_key=True)
    description = mongo.StringField(max_length=100)
    design = mongo.EmbeddedDocumentField(Design)
    technology = mongo.EmbeddedDocumentField(Technology)
    flows = mongo.ListField(mongo.EmbeddedDocumentField(Flow))

    def extract_metrics(self):
        logger = get_logger()
        logger.info('Starting metrics collection process .. ')
    
        for flow in self.flows:
            for stage in flow.stages:
                tool = registered_tool(stage.tool.name)
                
                if tool is not None:
                    if stage.tool.version in tool['versions']:
                        logger.info('%s parser successfully loaded', stage.tool.name)
                        stage.metrics = tool['versions'][stage.tool.version](stage.log_file)
                    else:
                        logger.warn('Tool %s is recognized, but version %s is not registered - will use default version %s', \
                            stage.tool.name, stage.tool.version, tool['default_version'])
                        stage.metrics = tool['versions'][tool['default_version']](stage.log_file)
                            
                else:
                    logger.error('Tool %s is not recognized!', stage.tool.name)
                    exit()
        
