using System;

namespace DataStructures.Trees
{
    public interface INode<TData> where TData: IComparable<TData>
    {
         INode<TData> Left { get; }

         INode<TData> Right { get; }

         INode<TData> Parent { get; }

        TData Data { get; }
    }
}