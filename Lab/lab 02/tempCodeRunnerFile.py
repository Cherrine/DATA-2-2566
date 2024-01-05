    def print_stack(self):
        """print stack"""
        print(', '.join(f"'{i}'" if isinstance(i, str) else str(i) for i in self.stack))