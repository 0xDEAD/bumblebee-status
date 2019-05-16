"""Check updates to Arch Linux."""


import subprocess
import bumblebee.input
import bumblebee.output
import bumblebee.engine


class Module(bumblebee.engine.Module):
    def __init__(self, engine, config):
        widget = bumblebee.output.Widget(full_text=self.utilization)
        super(Module, self).__init__(engine, config, widget)
        self.packages = self.check_updates()
        engine.input.register_callback(self, button=bumblebee.input.LEFT_MOUSE, cmd="/home/matthias/.local/bin/jump-to-gmail.sh")

    def check_updates(self):
        p = subprocess.Popen("~/bin/gmail.bash", stdout=subprocess.PIPE, shell=True)
        p_status = p.wait()

        if p_status == 0:
            (output, err) = p.communicate()

            output = output.decode('utf-8')
            return int(output)
        return 0

    def utilization(self, widget):
        return 'GMail: {}'.format(self.packages)

    def hidden(self):
            return self.check_updates() == 0

    def update(self, widgets):
        self.packages = self.check_updates()

    def state(self, widget):
        return self.threshold_state(self.packages, 1, 100)

