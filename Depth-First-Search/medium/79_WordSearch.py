class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        initials_list = []
        i_max = len(board)
        j_max = len(board[0])
        for i in range(i_max):
            for j in range(j_max):
                if board[i][j] == word[0]:
                    initials_list.append((i, j))
        # answers = []
        for i, j in initials_list:
            visiting = set()
            current_index = 0
            if self.DFS(board, i, j, word, current_index, visiting, i_max, j_max):
                return True
        return False
    def DFS(self, board, i, j, word, current_index, visiting, i_max, j_max):
        if current_index == len(word) - 1:
            # answers.append(word_up_to_now[:])
            return True
        if (i, j) in visiting:
            return False
        visiting.add((i, j))
        neighbors = [(i+1 ,j), (i-1, j), (i, j+1), (i, j-1)]
        for n_i, n_j in neighbors:
            if n_i >= 0 and n_i < i_max and n_j >= 0 and n_j < j_max and board[n_i][n_j] == word[current_index+1] and (n_i, n_j) not in visiting:
                    if self.DFS(board, n_i, n_j, word, current_index + 1, visiting, i_max, j_max):
                        return True
        visiting.remove((i, j))
        return False