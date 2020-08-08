# 命令模式：将请求封装成对象，这可以让你使用不同的请求、队列，或者日志请求来参数化其他对象。命令模式也可以支持撤销操作。


# 代码实现
from abc import ABC, abstractmethod


# 灯
class Light:
    def on(self):
        print('Light is on.')

    def off(self):
        print('Light is off.')


# 风扇
class CeilingFan:
    def on(self):
        print('CeilingFan is on.')

    def off(self):
        print('CeilingFan is off.')


# 命令（接口类）
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


# 空命令（实现类）
class NoCommand(Command):
    def execute(self):
        pass

    def undo(self):
        pass


# 开灯命令（实现类）
class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()


# 关灯命令（实现类）
class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()


# 开风扇命令（实现类）
class CeilingFanOnCommand(Command):
    def __init__(self, ceilingfan: CeilingFan):
        self.ceilingfan = ceilingfan

    def execute(self):
        self.ceilingfan.on()

    def undo(self):
        self.ceilingfan.off()


# 关风扇命令（实现类）
class CeilingFanOffCommand(Command):
    def __init__(self, ceilingfan: CeilingFan):
        self.ceilingfan = ceilingfan

    def execute(self):
        self.ceilingfan.off()

    def undo(self):
        self.ceilingfan.on()


# 简单遥控器
class SimpleRemoteControl:
    def set_command(self, command: Command):
        self.slot = command

    def button_was_pressed(self):
        self.slot.execute()


# 高级点的遥控器（包含多个开和关按键）
class RemoteControl:
    def __init__(self):
        self.on_commands = dict()
        self.off_commands = dict()

    def set_command(self, slot: int, on_command: Command, off_command: Command):
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    def on_button_was_pushed(self, slot: int):
        self.on_commands[slot].execute()

    def off_button_was_pushed(self, slot: int):
        self.off_commands[slot].execute()


# 更高级点的遥控器（包含撤销按键）
# 假设有5个按键：开/关灯、开/关风扇和撤销
class RemoteControlWithUndo:
    def __init__(self):
        self.on_commands = dict()
        self.off_commands = dict()
        for i in range(2):
            self.on_commands[i] = NoCommand()
            self.off_commands[i] = NoCommand()
        self.undo_command = NoCommand()

    def set_command(self, slot: int, on_command: Command, off_command: Command):
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    def on_button_was_pushed(self, slot: int):
        self.on_commands[slot].execute()
        self.undo_command = self.on_commands[slot]

    def off_button_was_pushed(self, slot: int):
        self.off_commands[slot].execute()
        self.undo_command = self.off_commands[slot]

    def undo_button_was_pushed(self):
        self.undo_command.undo()


# 宏命令
class MacroCommand(Command):
    def __init__(self, commands: list):
        self.commands = commands

    def execute(self):
        for command in self.commands:
            command.execute()

    def undo(self):
        for command in self.commands:
            command.undo()


if __name__ == '__main__':
    ##
    # ================== Test1 ==================
    ##
    # remote = SimpleRemoteControl()
    # # remote.set_command(LightOnCommand(Light()))
    # remote.set_command(LightOffCommand(Light()))
    # remote.button_was_pressed()

    ##
    # ================== Test2 ==================
    ##
    # remote = RemoteControl()
    # remote.set_command(0, LightOnCommand(Light()), LightOffCommand(Light()))
    # remote.set_command(1, CeilingFanOnCommand(CeilingFan()), CeilingFanOffCommand(CeilingFan()))
    #
    # remote.on_button_was_pushed(0)
    # remote.off_button_was_pushed(0)
    # remote.on_button_was_pushed(1)
    # remote.off_button_was_pushed(1)

    ##
    # ================== Test3 ==================
    ##
    # remote = RemoteControlWithUndo()
    # remote.set_command(0, LightOnCommand(Light()), LightOffCommand(Light()))
    # remote.set_command(1, CeilingFanOnCommand(CeilingFan()), CeilingFanOffCommand(CeilingFan()))
    #
    # remote.on_button_was_pushed(0)
    # remote.undo_button_was_pushed()
    #
    # remote.on_button_was_pushed(1)
    # remote.undo_button_was_pushed()
    #
    # remote.off_button_was_pushed(0)
    # remote.undo_button_was_pushed()
    #
    # remote.off_button_was_pushed(1)
    # remote.undo_button_was_pushed()

    ##
    # ================== Test3 ==================
    ##
    party_on = [LightOnCommand(Light()), CeilingFanOnCommand(CeilingFan())]
    party_off = [LightOffCommand(Light()), CeilingFanOffCommand(CeilingFan())]
    party_on_macro = MacroCommand(party_on)
    party_on_macro.execute()
    party_on_macro.undo()
    party_off_macro = MacroCommand(party_off)
    party_off_macro.execute()
    party_off_macro.undo()
