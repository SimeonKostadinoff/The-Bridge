import React from 'react';
import CommentForm from '../components/CommentForm';
import CommentRepresentation from '../components/CommentRepresentation';

export default (props) => {
    const data = props.data.map(post =>
      <div key={post.id} className="posts-dashboard">
      <div>
        <a href={"//localhost:8000/customer/organisations/" + post.organisation.id} className="post-title">{post.organisation.title}</a>
        <span className="post-comment-dateTime">{post.timestamp}</span>
      </div>
        <div className="post-description">{post.description}</div>
        <CommentRepresentation comments={props.comments} postId={post.id} showCommentsForPost={props.showCommentsForPost}/>
        <CommentForm postId={post.id} addCurrentComment={props.addCurrentComment}/>
      </div>
    )
    return <div>
        {data}
    </div>
}