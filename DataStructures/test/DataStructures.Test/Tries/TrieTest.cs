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

        [Fact]
        public void Delete_ExisingWord_ReturnsTrue()
        {
            // Arrange
            Trie trie = new Trie();
            trie.Add("test");
            trie.Add("testing");
            trie.Add("abc");

            // Act
            bool isSuccessful = trie.Remove("test");

            // Assert
            Assert.True(isSuccessful);
            Assert.True(trie.Contains("testing", true));
            Assert.True(trie.Contains("abc", true));
        }

        [Theory]
        [InlineData("tes")]
        [InlineData("testi")]
        [InlineData("a")]
        [InlineData("bc")]
        public void Delete_NonExisingWord_ReturnsFalse(string wordToDelete)
        {
            // Arrange
            Trie trie = new Trie();
            trie.Add("test");
            trie.Add("testing");
            trie.Add("abc");

            // Act
            bool isSuccessful = trie.Remove(wordToDelete);

            // Assert
            Assert.False(isSuccessful);
            Assert.True(trie.Contains("testing", true));
            Assert.True(trie.Contains("test", true));
            Assert.True(trie.Contains("abc", true));
        }
    }
}