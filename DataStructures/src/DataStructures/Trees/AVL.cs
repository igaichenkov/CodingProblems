using System;
using System.Collections.Generic;

namespace DataStructures.Trees
{
    public class AVL<TData> where TData: IComparable<TData>
    {
        private Node<TData> _root;

        public INode<TData> Root => _root;

        public INode<TData> Add(TData data)
        {
            if (data == null)
            {
                throw new ArgumentNullException(nameof(data));
            }

            var newNode = new Node<TData>(data);
            if (_root == null)
            {
                _root = newNode;
            }
            else
            {
                Add(_root, newNode);
            }

            return newNode;
        }

        public INode<TData> Find(TData toFind)
        {
            if (toFind == null)
            {
                throw new ArgumentNullException(nameof(toFind));
            }

            return Find(_root, toFind);
        }

        public void Remove(TData toRemove)
        {
            var nodeToRemove = Find(_root, toRemove);
            Remove(nodeToRemove);
        }

        private void Add(Node<TData> node, Node<TData> newNode)
        {
            if (newNode.Data.CompareTo(node.Data) > 0)
            {
                if (node.Right == null)
                {
                    node.Right = newNode;
                    newNode.Parent = node;
                    return;
                }

                Add(node.Right, newNode);
            }
            else
            {
                if (node.Left == null)
                {
                    node.Left = newNode;
                    newNode.Parent = node;
                    return;
                }

                Add(node.Left, newNode);
            }

            node.UpdateHeights();
            CheckBalance(node);
        }

        private void Remove(Node<TData> nodeToRemove)
        {
            if (nodeToRemove == null)
            {
                return;
            }

            if (nodeToRemove.IsLeafNode)
            {
                RemoveLeafNode(nodeToRemove);
            }
            else if (nodeToRemove.Left != null && nodeToRemove.Right != null)
            {
                Node<TData> smallestRightChild = FindSmallestChild(nodeToRemove.Right);
                nodeToRemove.Data = smallestRightChild.Data;

                Remove(smallestRightChild);
                return;
            }
            else
            {
                RemoveNodeWithOneChild(nodeToRemove);
            }

            EnsureBalanced(nodeToRemove.Parent);
        }

        private void EnsureBalanced(Node<TData> node)
        {
            while (node != null)
            {
                node.UpdateHeights();
                CheckBalance(node);
                node = node.Parent;
            }
        }

        private static void RemoveNodeWithOneChild(Node<TData> nodeToRemove)
        {
            Node<TData> successor = nodeToRemove.HasRightNodeOnly
                            ? nodeToRemove.Right
                            : nodeToRemove.Left;

            successor.Parent = nodeToRemove.Parent;
            if (nodeToRemove.IsLeftSubTreeNode)
            {
                nodeToRemove.Parent.Left = successor;
            }
            else
            {
                nodeToRemove.Parent.Right = successor;
            }
        }

        private static Node<TData> FindSmallestChild(Node<TData> node)
        {
            while (node.Left != null)
            {
                node = node.Left;
            }

            return node;
        }

        private static void RemoveLeafNode(Node<TData> nodeToRemove)
        {
            if (nodeToRemove.IsLeftSubTreeNode)
            {
                nodeToRemove.Parent.Left = null;
            }
            else
            {
                nodeToRemove.Parent.Right = null;
            }
        }

        private Node<TData> Find(Node<TData> current, TData toFind)
        {
            if (current == null)
            {
                return null;
            }

            int compareResult = toFind.CompareTo(current.Data);

            if (compareResult == 0)
            {
                return current;
            }

            if (compareResult < 0)
            {
                return Find(current.Left, toFind);
            }

            return Find(current.Right, toFind);
        }

        private void CheckBalance(Node<TData> node)
        {
            if (node.Right != null)
            {
                node.Right = Rebalance(node.Right);
                node.Right.Parent = node;
            }

            if (node.Left != null)
            {
                node.Left = Rebalance(node.Left);
                node.Left.Parent = node;
            }        

            if (node == _root)
            {
                _root = Rebalance(_root);
                _root.Parent = null;
            }

            node.UpdateHeights();
        }
        
        private Node<TData> Rebalance(Node<TData> node)
        {
            if (node == null || Math.Abs(node.LeftHeight - node.RightHeight) <= 1)
            {
                return node;
            }

            if (node.LeftHeight > node.RightHeight)
            {
                if (node.Left.LeftHeight > node.Left.RightHeight)
                {
                    return RotateRight(node);
                }
             
                return RotateLeftRight(node);
            }
            
            if (node.Right.RightHeight > node.Right.LeftHeight)
            {
                return RotateLeft(node);
            }
            
            return RotateRightLeft(node);
        }

        private Node<TData> RotateRight(Node<TData> node)
        {
            var tmp = node.Left;
            node.Left = tmp.Right;

            if (tmp.Right != null)
            {
                tmp.Right.Parent = node;
            }

            tmp.Right = node;
            node.Parent = tmp;

            node.UpdateHeights();
            tmp.UpdateHeights();

            return tmp;
        }

        private Node<TData> RotateLeft(Node<TData> node)
        {
            var tmp = node.Right;
            node.Right = tmp.Left;

            if (tmp.Left != null)
            {
                tmp.Left.Parent = node;
            }

            tmp.Left = node;
            node.Parent = tmp;

            node.UpdateHeights();
            tmp.UpdateHeights();

            return tmp;
        }

        private Node<TData> RotateLeftRight(Node<TData> node)
        {
            node.Left = RotateLeft(node.Left);
            node.Left.Parent = node;

            return RotateRight(node);
        }

        private Node<TData> RotateRightLeft(Node<TData> node)
        {
            node.Right = RotateRight(node.Right);
            node.Right.Parent = node;

            return RotateLeft(node);
        }
    }
}