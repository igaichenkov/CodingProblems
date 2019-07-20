using System;

namespace DataStructures.Trees
{
    public class AVL<TData> where TData: IComparable<TData>
    {
        private Node<TData> _root;

        public INode<TData> Root => _root;

        public INode<TData> Add(TData data)
        {
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

        private void Add(Node<TData> node, Node<TData> newNode)
        {
            if (newNode.Data.CompareTo(node.Data) > 0)
            {
                if (node.Right == null)
                {
                    node.Right = newNode;
                    return;
                }

                Add(node.Right, newNode);
            }
            else
            {
                if (node.Left == null)
                {
                    node.Left = newNode;
                    return;
                }

                Add(node.Left, newNode);
            }

            node.UpdateHeights();
            CheckBalance(node);
        }

        private void CheckBalance(Node<TData> node)
        {
            node.Right = Rebalance(node.Right);
            node.Left = Rebalance(node.Left);

            if (node == _root)
            {
                _root = Rebalance(_root);
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

            tmp.Right = node;

            node.UpdateHeights();
            tmp.UpdateHeights();

            return tmp;
        }

        private Node<TData> RotateLeft(Node<TData> node)
        {
            var tmp = node.Right;
            node.Right = tmp.Left;
            tmp.Left = node;

            node.UpdateHeights();
            tmp.UpdateHeights();

            return tmp;
        }

        private Node<TData> RotateLeftRight(Node<TData> node)
        {
            node.Left = RotateLeft(node.Left);
            return RotateRight(node);
        }

        private Node<TData> RotateRightLeft(Node<TData> node)
        {
            node.Right = RotateRight(node.Right);
            return RotateLeft(node);
        }
    }

    internal class Node<TData> : INode<TData> where TData: IComparable<TData>
    {
        private Node<TData> _left;
        private Node<TData> _right;

        public TData Data { get; }

        public Node<TData> Left 
        { 
            get => _left;
            set
            {
                _left = value;
                UpdateHeights();
            }
        }

        public Node<TData> Right 
        { 
            get => _right;
            set
            {
                _right = value;
                UpdateHeights();
            }
        }

        public int LeftHeight { get; set; }

        public int RightHeight { get; set; }

        public int MaxHeight => Math.Max(LeftHeight, RightHeight);

        INode<TData> INode<TData>.Left => _left;

        INode<TData> INode<TData>.Right => _right;

        public void UpdateHeights()
        {
            if (Left == null)
            {
                LeftHeight = 0;
            }
            else
            {
                LeftHeight = Left.MaxHeight + 1;
            }

            if (Right == null)
            {
                RightHeight = 0;
            }
            else
            {
                RightHeight = Right.MaxHeight + 1;
            }
        }

        public Node(TData data)
        {
            Data = data;
        }

        public override string ToString() 
        {
            return Data.ToString();
        }
    }
}