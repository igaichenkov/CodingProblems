using System.Collections.Generic;

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

        public bool Remove(string word)
        {
            TrieNode node = _root;
            var traversalStack = new Stack<TrieNode>();
            traversalStack.Push(_root);

            for (int i = 0; i < word.Length; i++)
            {
                traversalStack.Push(node);

                if (!node.Children.TryGetValue(word[i], out node))
                {
                    return false;
                }
            }

            if (!node.IsEndOfWord)
            {
                return false;
            }

            int index = word.Length - 1;
            while (traversalStack.Count > 0)
            {
                var nextNode = traversalStack.Pop();
                if (node.Children.Count > 0)
                {
                    node.IsEndOfWord = false;
                }
                else
                {
                    nextNode.Children.Remove(word[index]);
                }
                
                node = nextNode;
                index--;
            }

            return true;
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