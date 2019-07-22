namespace DataStructures.Tries
{
    public class Trie
    {
        private readonly TrieNode _root;

        public Trie()
        {
            _root = new TrieNode();
        }

        public void Add(string word)
        {
            if (word is null)
            {
                throw new System.ArgumentNullException(nameof(word));
            }

            TrieNode node = _root;

            for (int i = 0; i < word.Length; i++)
            {
                if (!node.Children.ContainsKey(word[i]))
                {
                    TrieNode newNode = new TrieNode();
                    node.Children.Add(word[i], newNode);
                }

                node = node.Children[word[i]];

                if (i == word.Length - 1)
                {
                    node.IsEndOfWord = true;
                }
            }
        }

        public void Remove(string word)
        {

        }

        public bool Contains(string prefix, bool asWholeWord = false)
        {
            TrieNode node = _root;
            int index = 0;

            while (true)
            {
                if (!node.Children.TryGetValue(prefix[index], out node))
                {
                    return false;
                }

                index++;
                if (index == prefix.Length)
                {
                    return !asWholeWord || node.IsEndOfWord;
                }
            }
        }
    }
}