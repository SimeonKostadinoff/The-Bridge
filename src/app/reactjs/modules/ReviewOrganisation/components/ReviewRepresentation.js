import React from 'react';
import StarRating from 'react-star-rating';

export default (props) => {
    const data = props.data.map(review =>
        <div key={review.id} className="posts-dashboard">
            <div>
                <span className="post-title">{review.author.first_name} {review.author.last_name}</span>
                <span className="reviewRating"><StarRating name="starrating" totalStars={5} size={20} rating={review.rating}/></span>
                <span className="post-comment-dateTime">{review.timestamp}</span>
            </div>
            <div className="post-description">{review.text}</div>
        </div>
    )
    return <div>
        {data}
    </div>
}