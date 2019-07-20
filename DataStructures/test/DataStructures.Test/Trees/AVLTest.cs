using Xunit;
using DataStructures.Trees;

namespace DataStructures.Test.Trees
{
    public class AVLTest
    {
        [Fact]
        public void TestCase()
        {
            // Arrange
            var tree = new AVL<int>();

            // Act
            tree.Add(43);
            tree.Add(18);
            tree.Add(22);
            tree.Add(9);
            tree.Add(21);
            tree.Add(6);
            tree.Add(8);
            tree.Add(20);
            tree.Add(63);
            tree.Add(50);
            tree.Add(62);
            tree.Add(51);
            
            // Assert
            Assert.Equal(22, tree.Root.Data);
            Assert.Equal(18, tree.Root.Left.Data);
            Assert.Equal(50, tree.Root.Right.Data);
            Assert.Equal(8, tree.Root.Left.Left.Data);
            Assert.Equal(21, tree.Root.Left.Right.Data);

            Assert.Equal(43, tree.Root.Right.Left.Data);
            Assert.Equal(62, tree.Root.Right.Right.Data);

            Assert.Equal(6, tree.Root.Left.Left.Left.Data);
            Assert.Equal(9, tree.Root.Left.Left.Right.Data);
            Assert.Equal(20, tree.Root.Left.Right.Left.Data);
        }
    }
}