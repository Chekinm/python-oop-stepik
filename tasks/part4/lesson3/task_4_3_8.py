class SoftList(list):
    
    def __getitem__(self, idx):

        if isinstance(idx, int) and (idx >= len(self) or idx < - len(self)):
            return False
        else:
            return self[idx]
