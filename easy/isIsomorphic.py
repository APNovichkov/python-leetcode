def isIsomorphic(self, s, t):
    """

    Time complexity: O(n) where n is the lenght of s and t. It is O(n) because
    we are running through string s and string t simultaneously

    Memory Complexity: O(n) because we are storing a map of each unique character
    to another unique character

    """

    m = {}

    m_string = ""
    for s_ch, t_ch in zip(s, t):
        if s_ch not in m.keys():
            if t_ch in m.values():
                return False
            m[s_ch] = t_ch
            m_string += (t_ch)
        else:
            m_string += (m[s_ch])

    return m_string == t
