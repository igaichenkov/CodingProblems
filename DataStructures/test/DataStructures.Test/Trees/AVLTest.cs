using Xunit;
using DataStructures.Trees;
using System.Collections.Generic;

namespace DataStructures.Test.Trees
{
    public class AVLTest
    {
        [Fact]
        public void Add_BuildsCorrectTree()
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
            Assert.Null(tree.Root.Parent);

            Assert.Equal(18, tree.Root.Left.Data);
            Assert.Equal(tree.Root, tree.Root.Left.Parent);

            Assert.Equal(50, tree.Root.Right.Data);
            Assert.Equal(tree.Root, tree.Root.Right.Parent);

            Assert.Equal(8, tree.Root.Left.Left.Data);
            Assert.Equal(tree.Root.Left, tree.Root.Left.Left.Parent);

            Assert.Equal(21, tree.Root.Left.Right.Data);
            Assert.Equal(tree.Root.Left, tree.Root.Left.Right.Parent);

            Assert.Equal(43, tree.Root.Right.Left.Data);
            Assert.Equal(tree.Root.Right, tree.Root.Right.Left.Parent);

            Assert.Equal(62, tree.Root.Right.Right.Data);
            Assert.Equal(tree.Root.Right, tree.Root.Right.Right.Parent);

            Assert.Equal(6, tree.Root.Left.Left.Left.Data);
            Assert.Equal(tree.Root.Left.Left, tree.Root.Left.Left.Left.Parent);

            Assert.Equal(9, tree.Root.Left.Left.Right.Data);
            Assert.Equal(tree.Root.Left.Left, tree.Root.Left.Left.Right.Parent);

            Assert.Equal(20, tree.Root.Left.Right.Left.Data);
            Assert.Equal(tree.Root.Left.Right, tree.Root.Left.Right.Left.Parent);
        }

        [Fact]
        public void Find_ValueExists_ReturnsNode()
        {
            // Arrange
            var tree = new AVL<int>();
            tree.Add(43);
            tree.Add(18);
            tree.Add(22);
            tree.Add(9);
            tree.Add(21);
            tree.Add(6);

            // Act
            INode<int> node = tree.Find(21);

            // Assert
            Assert.Equal(21, node.Data);
        }

        [Fact]
        public void Find_ValueDoesNotExist_ReturnsNull()
        {
            // Arrange
            AVL<int> tree = InitTree();

            // Act
            INode<int> node = tree.Find(20);

            // Assert
            Assert.Null(node);
        }

        [Fact]
        public void Remove_LeafNode_RunsTreeRebalance()
        {
            // Arrange
            AVL<int> tree = InitTree();

            // Act
            tree.Remove(6);

            // Assert
            AssertTree(tree, new[] { 22, 18, 43, 9, 21, 25 });
        }

        [Fact]
        public void Remove_RootNode_RunsTreeRebalance()
        {
            // Arrange
            AVL<int> tree = InitTree();

            // Act
            tree.Remove(18);

            // Assert
            AssertTree(tree, new[] { 21, 9, 25, 6, 22, 43 });
        }

        private static AVL<int> InitTree()
        {
            var tree = new AVL<int>();
            tree.Add(43);
            tree.Add(18);
            tree.Add(22);
            tree.Add(9);
            tree.Add(21);
            tree.Add(6);
            tree.Add(25);

            return tree;
        }

        private static void AssertTree(AVL<int> tree, int[] bfsTraversal)
        {
            Queue<INode<int>> traversalQueue = new Queue<INode<int>>();
            List<int> traversalResult = new List<int>();

            traversalQueue.Enqueue(tree.Root);

            while (traversalQueue.Count > 0)
            {
                INode<int> node = traversalQueue.Dequeue();
                traversalResult.Add(node.Data);

                if (node.Left != null)
                {
                    Assert.Equal(node, node.Left.Parent);
                    traversalQueue.Enqueue(node.Left);
                }

                if (node.Right != null)
                {
                    Assert.Equal(node, node.Right.Parent);
                    traversalQueue.Enqueue(node.Right);
                }
            }

            Assert.Equal(bfsTraversal, traversalResult.ToArray());
        }

    }
}