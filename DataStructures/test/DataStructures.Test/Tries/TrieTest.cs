using DataStructures.Tries;
using Xunit;

namespace DataStructures.Test.Tries
{
    public class TrieTest
    {
        [Theory]
        [InlineData("tes", false, true)]
        [InlineData("tes", true, false)]
        [InlineData("tet", false, true)]
        [InlineData("test", true, true)]
        public void AddContainsTest(string prefixToSearch, bool asWholeWord, bool expectedResult)
        {
            // Arrange
            Trie trie = new Trie();
            trie.Add("test");
            trie.Add("tett");

            // Act
            bool contains = trie.Contains(prefixToSearch, asWholeWord);

            // Assert
            Assert.Equal(expectedResult, contains);
        }
    }
}