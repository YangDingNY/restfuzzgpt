import sys
import os

# 获取当前文件的绝对路径
current_path = os.path.dirname(__file__)

# 获取上级目录的路径
parent_path = os.path.dirname(current_path)

# 将上级目录的路径添加到sys.path中
sys.path.append(parent_path)
from TestSequence import TestSequence
def testGetSequenceString():
    oneTestSequence = TestSequence(1, ["request1", "request2", "request3"])
    print(oneTestSequence.getSequenceString())

testGetSequenceString()