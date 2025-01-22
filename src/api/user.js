import serviceAxios from "@/api/index.js";

export const getUserInfo = (r) => {
    return serviceAxios({
        url: '/api/login/user/info' + (r ? '?r=' + r : ''),
        method: 'get',
    });
}
export const getScore = () => {
    return serviceAxios({
        url: '/api/user/score',
        method: 'get',
    });
}



export const getOtherUserInfoApi = (userId) => {
    return serviceAxios({
        url: '/api/user/info/' + userId,
        method: 'get',
    });
}

export const likeApi = (pictureId) => {
    return serviceAxios({
        url: `/api/picture/like`,
        method: 'post',
        data: {pictureId: pictureId}
    })
}

export const followApi = (userId) => {
    return serviceAxios({
        url: `/api/user/` + userId,
        method: 'post',
    })
}

export const getFanListApi = (fans, page) => {
    return serviceAxios({
        url: '/api/' + (fans ? 'fansList' : 'followList') + '?perPage=10&page='+page,
        method: 'get',
        ...{
            perPage: 10,
            page: page
        }
    })
}

export const getOrderLogApi = (page) => {
    return serviceAxios({
        url: '/api/oderList' + '?parPage=10&page=' + page,
        method: 'get',
    })
}

export const getScoreLogApi = (add, page) => {
    return serviceAxios({
        url: '/api/score/' + (add ? 'queryScoreAcquired' : 'queryScore') + '?page=' + page,
        method: 'post',
        contentType: 'application/json',
        data: {
            current: page || 1,
            size: 20
        },
    })
}

export const getUnReadMsgList = () => {
    return serviceAxios({
        url: '/api/notification/unRead',
        method: 'get',
    })
}

export const getMsgList = (page) => {
    return serviceAxios({
        url: '/api/notification/list?pageSize=10&page=' + page,
        method: 'get',
    })
}
export const readAllMsg = () => {
    return serviceAxios({
        url: '/api/notification/readAll',
        method: 'post',
    })
}

export const updateUserInfo = (avatar, userName) => {
    return serviceAxios({
        url: '/api/login/userdata/update',
        method: 'post',
        contentType: 'application/json',
        data:{
            avatar: avatar,
            userName: userName
        }
    })
}

export const getTaskListApi = () => {
    return serviceAxios({
        url: '/api/score/TaskSchedule',
        method: 'get',
        contentType: 'application/json',
    })
}


