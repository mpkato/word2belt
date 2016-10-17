# -*- coding: utf-8 -*-
import os
import json
class TestWord2BeltScript(object):

    def test_main(self):
        from subprocess import Popen, PIPE
        cmd = ("word2belt 京都 "
            + "--url=%s --username=%s --password=%s --filename=%s" % (
                os.environ["W2B_URL"], os.environ["W2B_USER"],
                os.environ["W2B_PASS"], "ohshima.txt"))
        p = Popen(cmd.split(' '), stdout=PIPE, stderr=PIPE)
        out, err = p.communicate()
        out = out.decode("utf-8")
        out = list(map(float, out.strip().split(" ")))
        assert out == [2.667307, -1.069066, -7.67362, 2.70062,
            -7.44677, 1.342252, -2.665191, 4.145811]
