#  first try:
# from time import sleep
# class Foo(object):
#     def __init__(self):
#         self.a_done = False
#         self.b_done = False
#         self.c_done = False


#     def first(self, printFirst):
#         """
#         :type printFirst: method
#         :rtype: void
#         """
        
#         # printFirst() outputs "first". Do not change or remove this line.
#         printFirst()
#         self.a_done = True


#     def second(self, printSecond):
#         """
#         :type printSecond: method
#         :rtype: void
#         """
#         while not self.a_done:
#             sleep(0.01)
#         # printSecond() outputs "second". Do not change or remove this line.
#         printSecond()
#         self.b_done = True
            
            
#     def third(self, printThird):
#         """
#         :type printThird: method
#         :rtype: void
#         """
#         while not self.b_done:
#             sleep(0.01)
#         # printThird() outputs "third". Do not change or remove this line.
#         printThird()
#         self.c_done = True

# better solution:
import threading
class Foo(object):
    def __init__(self):
        self.first_done = threading.Event()
        self.second_done = threading.Event()


    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first_done.set()


    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        self.first_done.wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.second_done.set()
            
            
    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        self.second_done.wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
    