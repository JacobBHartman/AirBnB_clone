#!/usr/bin/python3
"""
    this module contains the entry point of the command interpreter
"""


import cmd
import models
import shlex


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_create(self, arg):
        """ create a new instances of BaseModel, saves it to a JSON file
        and prints the 'id'.
        """
        if arg == "":
            print('** class name missing **')
        elif arg not in models.classes:
            print('** class doesn\'t exist **')
        else:
            new_model = models.classes[arg]()
            models.storage.save()
            print(new_model.id)

    def do_show(self, arg):
        """ Print the string representation of an instance based on the class
        name and 'id'
        """
        args = shlex.split(arg)
        try:
            if args[0] not in models.classes:
                raise NameError
            class_name = args[0]
        except IndexError:
            print("** class name missing **")
            return
        except NameError:
            print("** class doesn't exist **")
            return

        try:
            expected_id = args[1]
        except IndexError:
            print("** instance id missing **")
            return
        objs = models.storage.all()
        for obj_id, obj in objs.items():
            if obj.__class__.__name__ == class_name and obj.id == expected_id:
                print(obj)
                return
        print("** no instance found **")

    def do_destroy(self, arg):
        """ delete an instance based on the class name and 'id'
        (save the change into the JSON file)
        """
        args = shlex.split(arg)
        try:
            if args[0] not in models.classes:
                raise NameError
            class_name = args[0]
        except IndexError:
            print("** class name missing **")
            return
        except NameError:
            print("** class doesn't exist **")
            return
        try:
            expected_id = args[1]
        except IndexError:
            print("** instance id missing **")
            return
        objs = models.storage.all()
        for obj_id, obj in objs.items():
            if obj.__class__.__name__ == class_name and obj.id == expected_id:
                objs.pop(obj_id)
                models.storage.save()
                return
        print("** no instance found **")

    def do_all(self, arg):
        """ print all string representation of all instances based or not on
        the class name
        """
        try:
            new_list = []
            objs = models.storage.all()
            if arg == "":
                for obj in objs.values():
                    new_list.append(obj)
                print(new_list)
            else:
                if arg not in models.classes:
                    raise NameError
                for obj_id, obj in objs.items():
                    if obj.__class__.__name__ == arg:
                        new_list.append(obj)
                print(new_list)
        except NameError:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """ update an instance based on the class name and 'id' by adding or
        updating attribute
        """
        args = shlex.split(arg)

        try:
            if args[0] not in models.classes:
                raise NameError
            class_name = args[0]
        except IndexError:
            print("** class name missing **")
            return
        except NameError:
            print("** class doesn't exist **")
            return

        try:
            found = 0
            expected_id = args[1]
            objs = models.storage.all()
            for obj_id, obj in objs.items():
                if str(obj.id) == expected_id:
                    found = 1
                    obj_to_change = obj
                    break
            if found == 0:
                raise NameError
        except IndexError:
            print("** instance id missing **")
            return
        except NameError:
            print("** no instance found **")
            return

        try:
            expected_attr = args[2]
        except IndexError:
            print("** attribute name missing **")
            return

        try:
            setattr(obj_to_change, expected_attr, args[3])
        except IndexError:
            print("** value missing **")

        obj_to_change.save()

    def emptyline(self):
        """ Do nothing if empty line """
        pass

    def do_quit(self, arg):
        """ Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """ Quits the program """
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
