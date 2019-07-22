using System;

namespace DataStructures.Trees
{
    internal class Node<TData> : INode<TData> where TData: IComparable<TData>
    {
        private Node<TData> _left;
        private Node<TData> _right;

        public TData Data { get; set; }

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

        public Node<TData> Parent { get; set; }

        public int LeftHeight { get; set; }

        public int RightHeight { get; set; }

        public int MaxHeight => Math.Max(LeftHeight, RightHeight);

        public bool IsLeftSubTreeNode => Parent.Left == this;

        public bool IsLeafNode => Left == null && Right == null;

        public bool HasLeftNodeOnly => Left != null && Right == null;

        public bool HasRightNodeOnly => Left == null && Right != null;

        #region INode impl 
        INode<TData> INode<TData>.Left => _left;

        INode<TData> INode<TData>.Right => _right;

        INode<TData> INode<TData>.Parent => Parent;

        #endregion
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