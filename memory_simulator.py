class MemorySimulator:
    def __init__(self, frames):
        self.frames = frames
        self.memory = []
        self.page_faults = 0
        self.page_hits = 0

    def lru(self, pages):
        recent = []
        for p in pages:
            if p in self.memory:
                self.page_hits += 1
                recent.remove(p)
            else:
                self.page_faults += 1
                if len(self.memory) < self.frames:
                    self.memory.append(p)
                else:
                    old = recent.pop(0)
                    self.memory[self.memory.index(old)] = p
            recent.append(p)
            print("Access:", p, "Memory:", self.memory)

    def optimal(self, pages):
        for i in range(len(pages)):
            p = pages[i]
            if p in self.memory:
                self.page_hits += 1
            else:
                self.page_faults += 1
                if len(self.memory) < self.frames:
                    self.memory.append(p)
                else:
                    future = []
                    for m in self.memory:
                        if m in pages[i+1:]:
                            future.append(pages[i+1:].index(m))
                        else:
                            future.append(9999)
                    self.memory[future.index(max(future))] = p
            print("Access:", p, "Memory:", self.memory)


pages = list(map(int, input("Enter page reference string: ").split()))
frames = int(input("Enter number of frames: "))
algo = input("Enter algorithm (LRU / OPT): ").upper()

sim = MemorySimulator(frames)

if algo == "LRU":
    sim.lru(pages)
elif algo == "OPT":
    sim.optimal(pages)

print("Page Faults:", sim.page_faults)
print("Page Hits:", sim.page_hits)
