class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        initials_list = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    initials_list.append((i, j))
        answers = []
        for i, j in initials_list:
            visiting = set()
            word_up_to_now = [word[0]]
            self.DFS(board, i, j, word, word_up_to_now, visiting, answers)
        print(answers)
        for answer in answers:
            if answer:
                return True
        return False
    def DFS(self, board, i, j, word, word_up_to_now, visiting, answers):
        if len(word_up_to_now) == len(word):
            answers.append(word_up_to_now[:])
            return word_up_to_now
        i_max = len(board)
        j_max = len(board[0])
        if (i, j) in visiting:
            return
        visiting.add((i, j))
        neighbors = [(i+1 ,j), (i-1, j), (i, j+1), (i, j-1)]
        for neighbor in neighbors:
            if neighbor[0] >= 0 and neighbor[0] < i_max and neighbor[1] >= 0 and neighbor[1] < j_max and board[neighbor[0]][neighbor[1]] == word[len(word_up_to_now)] and (neighbor[0], neighbor[1]) not in visiting:
                    next_char = word[len(word_up_to_now)]
                    word_up_to_now.append(next_char)
                    self.DFS(board, neighbor[0], neighbor[1], word, word_up_to_now, visiting, answers)
                    word_up_to_now.pop()
        visiting.remove((i, j))
        return
Solution().exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB")