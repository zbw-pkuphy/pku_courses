class BinaryHeap:
    def __init__(self):
        self._heap = []
    def _perc_up(self,i):
        while (i-1)//2>=0:
            parent_idx=(i-1)//2
            if self._heap[i]<self._heap[parent_idx]:
                self._heap[i],self._heap[parent_idx]=self._heap[parent_idx],self._heap[i]
            i=parent_idx
    def insert(self,item):
        self._heap.append(item)
        self._perc_up(len(self._heap)-1)
    def _get_min_child(self,i):
        if 2*i+2>=len(self._heap):
            return 2*i+1
        else:
            if self._heap[2*i+1]<self._heap[2*i+2]:
                return 2*i+1
        return 2*i+2
    def _perc_down(self,i):
        while 2*i+1<len(self._heap):
            sm_child=self._get_min_child(i)
            if self._heap[i]>self._heap[sm_child]:
                self._heap[i],self._heap[sm_child]=self._heap[sm_child],self._heap[i]
            else:
                break
            i=sm_child
    def delete_min(self):
        self._heap[0],self._heap[-1]=self._heap[-1],self._heap[0]
        result=self._heap.pop()
        self._perc_down(0)
        return result
n=int(input())
heap=BinaryHeap()
for i in range(n):
    a=input()
    if a.startswith("1"):
        heap.insert(int(a.split()[1]))
    else:
        print(heap.delete_min())