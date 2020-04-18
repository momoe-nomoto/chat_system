S_ALONE = 0
S_TALKING = 1

# ==============================================================================
# Group class:
# member fields:
#   - An array of items, each a Member class
#   - A dictionary that keeps who is a chat group
# member functions:
#    - join: first time in
#    - leave: leave the system, and the group
#    - list_my_peers: who is in chatting with me?
#    - list_all: who is in the system, and the chat groups
#    - connect: connect to a peer in a chat group, and become part of the group
#    - disconnect: leave the chat group but stay in the system
# ==============================================================================


class Group:

    def __init__(self):
        self.members = {}
        self.chat_grps = {}
        self.grp_ever = 0

    def join(self, name):
        self.members[name] = S_ALONE
        return

    def is_member(self, name):

        # IMPLEMENTATION
        # ---- start your code ---- #
        if name in self.members.keys():
            return True
        return False
        # ---- end of your code --- #

    # implement
    def leave(self, name):
        """
        leave the system, and the group
        """
        # IMPLEMENTATION
        # ---- start your code ---- #
        try:
            del self.members[name]
        except KeyError:
            print(name, "not found")
        else:
            in_group, group_key = self.find_group(name)
            if in_group:
                self.chat_grps[group_key].remove(name)
        # ---- end of your code --- #
        return

    def find_group(self, name):
        """
        Auxiliary function internal to the class; return two
        variables: whether "name" is in a group, and if true
        the key to its group
        """

        found = False
        group_key = 0
        # IMPLEMENTATION
        # ---- start your code ---- #            
        for key, group in self.chat_grps.items():
            if name in group:
                found = True
                group_key = key
                break

        # ---- end of your code --- #
        return found, group_key

    def connect(self, me, peer):
        """
        me is alone, connecting peer.
        if peer is in a group, join it
        otherwise, create a new group with you and your peer
        """
        peer_in_group, group_key = self.find_group(peer)

        # IMPLEMENTATION
        # ---- start your code ---- #
        if me in self.members and peer in self.members: #In case someone accidentally adds someone not in system
            if peer_in_group:
                self.chat_grps[group_key].append(me)
                self.members[me] = S_TALKING
            else:
                self.grp_ever += 1
                self.chat_grps[self.grp_ever]=[me, peer]
                self.members[me] = self.members[peer] = S_TALKING
        else:
            print("{} or {} not found".format(me, peer))
        # ---- end of your code --- #
        return

    # implement
    def disconnect(self, me):
        """
        find myself in the group, quit, but stay in the system
        """
        # IMPLEMENTATION
        # ---- start your code ---- #
        if me in self.members: #Check if in system
            in_group, group_key = self.find_group(me)
            group_members = self.chat_grps[group_key]
            if in_group:
                group_members.remove(me)
                self.members[me] = S_ALONE
                if len(group_members) == 1:
                    self.members[group_members[0]] = S_ALONE
                    del group_members[0]
                    del self.chat_grps[group_key]
        else:
            print("{} or {} not found".format(me, peer))
        # ---- end of your code --- #
        return

    def list_all(self):
        # a simple minded implementation
        full_list = "Users: ------------" + "\n"
        full_list += str(self.members) + "\n"
        full_list += "Groups: -----------" + "\n"
        full_list += str(self.chat_grps) + "\n"
        return full_list

    # implement
    def list_me(self, me):
        """
        return a list, "me" followed by other peers in my group
        """
        my_list = []
        # IMPLEMENTATION
        # ---- start your code ---- #
        if me in self.members: #check if in system
            in_group, group_key = self.find_group(me)
            if in_group:
                my_list.append(me)
                for member in self.chat_grps[group_key]:
                    if member != me:
                        my_list.append(member)
        else:
            print(me, "not found")
        # ---- end of your code --- #
        return my_list

    def get_num_loners(self):
        """
        returns the number of loners in the system
        """
        num_loners = 0
        for m in self.members.values():
            if m == 0:
                num_loners += 1
        return num_loners

    def get_biggest_group(self):
        """
        returns the biggest group
        """
        return max(self.chat_grps.values(), key=len)

    def two_member_groups(self):
        """
        returns the groups with two members
        """
        return [group for group in self.chat_grps.values() if len(group) == 2]
        

if __name__ == "__main__":
    g = Group()
    g.join('a')
    g.join('b')
    g.join('c')
    g.join('d')
    print(g.list_all())

    g.connect('a', 'b')
    print(g.list_all())
    print("Groups with two members:", g.two_member_groups())
    print("Biggest group:", g.get_biggest_group())
    print()
    g.connect('c', 'a')
    print(g.list_all())
    
    print("Members in my group:", g.list_me('b'))
    print("Number of loners:", g.get_num_loners())
    print("Biggest group:", g.get_biggest_group())
    print("Groups with two members:", g.two_member_groups())
    print()
    g.leave('c')
    print(g.list_all())
    g.disconnect('b')
    print(g.list_all())
