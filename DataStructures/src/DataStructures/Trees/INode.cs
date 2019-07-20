using System;

namespace DataStructures.Trees
{
    public interface INode<TData> where TData: IComparable<TData>
    {
         INode<TData> Left { get; }

         INode<TData> Right { get; }

        TData Data { get; }
    }
}