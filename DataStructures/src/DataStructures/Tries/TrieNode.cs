using System.Collections.Generic;

namespace DataStructures.Tries
{
    internal class TrieNode
    {
        public Dictionary<char, TrieNode> Children { get; }

        public bool IsEndOfWord { get; set; }

        public TrieNode()
        {
            Children = new Dictionary<char, TrieNode>();
            IsEndOfWord = false;
        }
    }
}