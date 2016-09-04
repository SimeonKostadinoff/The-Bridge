export function showPostsResult(jsonResult) {
    return {
        type: "SHOW_POSTS",
        posts: jsonResult
    };
}

export function showCommentsResult(jsonResult, id) {
    return {
        type: "SHOW_COMMENTS",
        comments: jsonResult,
        id
    };
}

export function addCommentResult(comment, id) {
    return {
        type: "ADD_COMMENT",
        comment,
        id
    };
}

export function loadPosts() {
    return (dispatch, getState) => {
        let url = `http://localhost:8000/api/v1/posts/`;
        $.get(url, data => {
            dispatch(showPostsResult(data));
        });
    }
}

export function loadComments(post_id){
    return (dispatch, getState) => {
        let url = `http://localhost:8000/api/v1/comments/?post=${post_id}`
        $.get(url, data => {
            dispatch(showCommentsResult(data, post_id));
        });
    };
}

export function addCommentToPost(post_id, comment){
    function getCookie(name){
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                let cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function csrfSafeMethod(method){
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    return (dispatch, getState) => {
        let url = `http://localhost:8000/api/v1/comments/create/?type=user&post_id=${post_id}`
        let type = 'POST'
        
        $.ajax({
            type,
            url,
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                }
            },
            data: comment,
            success: (data) => {
                dispatch(addCommentResult(data, post_id))
            },
            error: (data) => {
                console.log(data);
            }
        });
    };
}

