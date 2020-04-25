def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        carry = 0
        to_continue = True

        out = ListNode()
        root = out

        while to_continue:
            if l2 is None:
                l2 = ListNode()
                l2.val = 0

            if l1 is None:
                l1 = ListNode()
                l1.val = 0

            res = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) // 10

            out.val = res

            if (l1.next is not None or l2.next is not None) or carry != 0:
                out.next = ListNode()
                out = out.next
            else:
                to_continue = False

            l1 = l1.next
            l2 = l2.next

        return root
