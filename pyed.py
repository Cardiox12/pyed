# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    pyed.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tony <tony@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/21 22:40:43 by tony              #+#    #+#              #
#    Updated: 2020/04/22 00:08:39 by tony             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from enum import Enum

class Mode(Enum):
    EDIT = 0
    NORMAL = 1

modes = ["Edit", "Normal"]

class Editor(object):
    def __init__(self):
        self.buffer = []
        self.clipboard = []
        self.current_file = None
        self.file_buffer = None
        self.mode = Mode.NORMAL.value

        self.commands = {
            "open" : "!open"
        }

    def edit_bar(self):
        pass

    def interpret_command(self, cmd):
        pass

    def open(self, filename):
        pass

    def search(self, needle):
        pass

    def append(self):
        pass

    def save(self):
        pass

    def insert(self, text, index):
        pass