class Stact (object):
    def __init__(self, limit=10):
        self.stact = []
        self.limit = limit

    def push(self, data):
        if len(self.stact) >= self.limit:
            stact2 = []
            for i in range(self.limit):
                stact2.append(self.stact[i])
            del self.stact[:]
            self.stact = stact2
            self.limit *= 2
            del stact2

        self.stact.append(data)

    def pop(self):
        if self.stact:
            pop_size = round(self.limit/2)
            if len(self.stact) <= pop_size:
                stact2 = []
                for i in range(len(self.stact)):
                    stact2.append(self.stact[i])
                del self.stact[:]
                self.stact = stact2
                self.limit /= 2
                del stact2

            return self.stact.pop()
        else:
            print('stact boş')

    def top(self):
        if self.stact:
            return self.stact[-1]
        else:
            print('stact boş')

    def is_empty(self):
        return not bool(self.stact)

    def size(self):
        return len(self.stact)

    def stack_print(self):
        print("Boyut:", self.limit)
        for i in range(len(self.stact)):
            print(self.stact[i])


if __name__ == '__main__':
    st = Stact()
    for i in range(0, 20):
        st.push(i)
    print(st.stact)
    st.pop()
    st.stack_print()
    print(st.is_empty())
    print(st.size())
    print(st.top())
    st.push(50)
    st.stack_print()

    for j in range(0, 19):
        st.pop()

    st.stack_print()

