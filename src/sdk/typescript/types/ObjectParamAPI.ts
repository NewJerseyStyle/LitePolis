import { ResponseContext, RequestContext, HttpFile, HttpInfo } from '../http/http';
import { Configuration} from '../configuration'

import { CommentModel } from '../models/CommentModel';
import { CommentResponse } from '../models/CommentResponse';
import { CommentResponseMessage } from '../models/CommentResponseMessage';
import { ConversationModel } from '../models/ConversationModel';
import { ConversationResponse } from '../models/ConversationResponse';
import { ConversationResponseMessage } from '../models/ConversationResponseMessage';
import { Detail } from '../models/Detail';
import { Detail1 } from '../models/Detail1';
import { Detail2 } from '../models/Detail2';
import { HTTPValidationError } from '../models/HTTPValidationError';
import { ResponseMessage } from '../models/ResponseMessage';
import { UserProfile } from '../models/UserProfile';
import { UserResponseMessage } from '../models/UserResponseMessage';
import { ValidationError } from '../models/ValidationError';
import { ValidationErrorLocInner } from '../models/ValidationErrorLocInner';

import { ObservableAPIKeysApi } from "./ObservableAPI";
import { APIKeysApiRequestFactory, APIKeysApiResponseProcessor} from "../apis/APIKeysApi";

export interface APIKeysApiUpdateUsertokenApiV1SecureUsersRenewPutRequest {
}

export class ObjectAPIKeysApi {
    private api: ObservableAPIKeysApi

    public constructor(configuration: Configuration, requestFactory?: APIKeysApiRequestFactory, responseProcessor?: APIKeysApiResponseProcessor) {
        this.api = new ObservableAPIKeysApi(configuration, requestFactory, responseProcessor);
    }

    /**
     * Updates the API key for the currently authenticated user.  Parameters ---------- user : dict     A dictionary containing user information retrieved     from the `get_user` dependency from `auth` module.     The dictionary is expected     to have the following structure:     ```     {         \'id\': <user_id>,         \'email\': <user_email>,         \'role\': <user_role>     }     ```  Returns ------- ResponseMessage     `detail` is the string of the new API key.
     * Update Usertoken
     * @param param the request object
     */
    public updateUsertokenApiV1SecureUsersRenewPutWithHttpInfo(param: APIKeysApiUpdateUsertokenApiV1SecureUsersRenewPutRequest = {}, options?: Configuration): Promise<HttpInfo<ResponseMessage>> {
        return this.api.updateUsertokenApiV1SecureUsersRenewPutWithHttpInfo( options).toPromise();
    }

    /**
     * Updates the API key for the currently authenticated user.  Parameters ---------- user : dict     A dictionary containing user information retrieved     from the `get_user` dependency from `auth` module.     The dictionary is expected     to have the following structure:     ```     {         \'id\': <user_id>,         \'email\': <user_email>,         \'role\': <user_role>     }     ```  Returns ------- ResponseMessage     `detail` is the string of the new API key.
     * Update Usertoken
     * @param param the request object
     */
    public updateUsertokenApiV1SecureUsersRenewPut(param: APIKeysApiUpdateUsertokenApiV1SecureUsersRenewPutRequest = {}, options?: Configuration): Promise<ResponseMessage> {
        return this.api.updateUsertokenApiV1SecureUsersRenewPut( options).toPromise();
    }

}

import { ObservableCommentsApi } from "./ObservableAPI";
import { CommentsApiRequestFactory, CommentsApiResponseProcessor} from "../apis/CommentsApi";

export interface CommentsApiCreateCommentApiV1SecureCommentsPostRequest {
    /**
     * 
     * @type CommentModel
     * @memberof CommentsApicreateCommentApiV1SecureCommentsPost
     */
    commentModel: CommentModel
}

export interface CommentsApiDeleteCommentApiV1SecureCommentsCidDeleteRequest {
    /**
     * 
     * @type number
     * @memberof CommentsApideleteCommentApiV1SecureCommentsCidDelete
     */
    cid: number
}

export interface CommentsApiGetCommentsApiV1SecureCommentsCidGetRequest {
    /**
     * 
     * @type number
     * @memberof CommentsApigetCommentsApiV1SecureCommentsCidGet
     */
    cid: number
    /**
     * 
     * @type boolean
     * @memberof CommentsApigetCommentsApiV1SecureCommentsCidGet
     */
    random?: boolean
    /**
     * 
     * @type boolean
     * @memberof CommentsApigetCommentsApiV1SecureCommentsCidGet
     */
    moderated?: boolean
}

export interface CommentsApiGetCommentsForModerationApiV1SecureCommentsCidModerateGetRequest {
    /**
     * 
     * @type number
     * @memberof CommentsApigetCommentsForModerationApiV1SecureCommentsCidModerateGet
     */
    cid: number
}

export interface CommentsApiUpdateCommentApiV1SecureCommentsPutRequest {
    /**
     * 
     * @type CommentModel
     * @memberof CommentsApiupdateCommentApiV1SecureCommentsPut
     */
    commentModel: CommentModel
}

export class ObjectCommentsApi {
    private api: ObservableCommentsApi

    public constructor(configuration: Configuration, requestFactory?: CommentsApiRequestFactory, responseProcessor?: CommentsApiResponseProcessor) {
        this.api = new ObservableCommentsApi(configuration, requestFactory, responseProcessor);
    }

    /**
     * Create a new comment.
     * Create Comment
     * @param param the request object
     */
    public createCommentApiV1SecureCommentsPostWithHttpInfo(param: CommentsApiCreateCommentApiV1SecureCommentsPostRequest, options?: Configuration): Promise<HttpInfo<any>> {
        return this.api.createCommentApiV1SecureCommentsPostWithHttpInfo(param.commentModel,  options).toPromise();
    }

    /**
     * Create a new comment.
     * Create Comment
     * @param param the request object
     */
    public createCommentApiV1SecureCommentsPost(param: CommentsApiCreateCommentApiV1SecureCommentsPostRequest, options?: Configuration): Promise<any> {
        return this.api.createCommentApiV1SecureCommentsPost(param.commentModel,  options).toPromise();
    }

    /**
     * Delete Comment
     * @param param the request object
     */
    public deleteCommentApiV1SecureCommentsCidDeleteWithHttpInfo(param: CommentsApiDeleteCommentApiV1SecureCommentsCidDeleteRequest, options?: Configuration): Promise<HttpInfo<any>> {
        return this.api.deleteCommentApiV1SecureCommentsCidDeleteWithHttpInfo(param.cid,  options).toPromise();
    }

    /**
     * Delete Comment
     * @param param the request object
     */
    public deleteCommentApiV1SecureCommentsCidDelete(param: CommentsApiDeleteCommentApiV1SecureCommentsCidDeleteRequest, options?: Configuration): Promise<any> {
        return this.api.deleteCommentApiV1SecureCommentsCidDelete(param.cid,  options).toPromise();
    }

    /**
     * Get Comments
     * @param param the request object
     */
    public getCommentsApiV1SecureCommentsCidGetWithHttpInfo(param: CommentsApiGetCommentsApiV1SecureCommentsCidGetRequest, options?: Configuration): Promise<HttpInfo<CommentResponse>> {
        return this.api.getCommentsApiV1SecureCommentsCidGetWithHttpInfo(param.cid, param.random, param.moderated,  options).toPromise();
    }

    /**
     * Get Comments
     * @param param the request object
     */
    public getCommentsApiV1SecureCommentsCidGet(param: CommentsApiGetCommentsApiV1SecureCommentsCidGetRequest, options?: Configuration): Promise<CommentResponse> {
        return this.api.getCommentsApiV1SecureCommentsCidGet(param.cid, param.random, param.moderated,  options).toPromise();
    }

    /**
     * Get comments waiting for moderation from a conversation.  Returns ------- dict     A dictionary containing comments waiting for moderation.
     * Get Comments For Moderation
     * @param param the request object
     */
    public getCommentsForModerationApiV1SecureCommentsCidModerateGetWithHttpInfo(param: CommentsApiGetCommentsForModerationApiV1SecureCommentsCidModerateGetRequest, options?: Configuration): Promise<HttpInfo<CommentResponse>> {
        return this.api.getCommentsForModerationApiV1SecureCommentsCidModerateGetWithHttpInfo(param.cid,  options).toPromise();
    }

    /**
     * Get comments waiting for moderation from a conversation.  Returns ------- dict     A dictionary containing comments waiting for moderation.
     * Get Comments For Moderation
     * @param param the request object
     */
    public getCommentsForModerationApiV1SecureCommentsCidModerateGet(param: CommentsApiGetCommentsForModerationApiV1SecureCommentsCidModerateGetRequest, options?: Configuration): Promise<CommentResponse> {
        return this.api.getCommentsForModerationApiV1SecureCommentsCidModerateGet(param.cid,  options).toPromise();
    }

    /**
     * Update a comment.
     * Update Comment
     * @param param the request object
     */
    public updateCommentApiV1SecureCommentsPutWithHttpInfo(param: CommentsApiUpdateCommentApiV1SecureCommentsPutRequest, options?: Configuration): Promise<HttpInfo<any>> {
        return this.api.updateCommentApiV1SecureCommentsPutWithHttpInfo(param.commentModel,  options).toPromise();
    }

    /**
     * Update a comment.
     * Update Comment
     * @param param the request object
     */
    public updateCommentApiV1SecureCommentsPut(param: CommentsApiUpdateCommentApiV1SecureCommentsPutRequest, options?: Configuration): Promise<any> {
        return this.api.updateCommentApiV1SecureCommentsPut(param.commentModel,  options).toPromise();
    }

}

import { ObservableConversationsApi } from "./ObservableAPI";
import { ConversationsApiRequestFactory, ConversationsApiResponseProcessor} from "../apis/ConversationsApi";

export interface ConversationsApiCreateConversationApiV1SecureConversationsPostRequest {
    /**
     * 
     * @type ConversationModel
     * @memberof ConversationsApicreateConversationApiV1SecureConversationsPost
     */
    conversationModel: ConversationModel
}

export interface ConversationsApiDeleteConversationApiV1SecureConversationsCidDeleteRequest {
    /**
     * 
     * @type number
     * @memberof ConversationsApideleteConversationApiV1SecureConversationsCidDelete
     */
    cid: number
}

export interface ConversationsApiGetAllConversationsApiV1SecureConversationsAllGetRequest {
}

export interface ConversationsApiGetConversationApiV1SecureConversationsCidGetRequest {
    /**
     * 
     * @type number
     * @memberof ConversationsApigetConversationApiV1SecureConversationsCidGet
     */
    cid: number
}

export interface ConversationsApiUpdateConversationApiV1SecureConversationsPutRequest {
    /**
     * 
     * @type ConversationModel
     * @memberof ConversationsApiupdateConversationApiV1SecureConversationsPut
     */
    conversationModel: ConversationModel
}

export class ObjectConversationsApi {
    private api: ObservableConversationsApi

    public constructor(configuration: Configuration, requestFactory?: ConversationsApiRequestFactory, responseProcessor?: ConversationsApiResponseProcessor) {
        this.api = new ObservableConversationsApi(configuration, requestFactory, responseProcessor);
    }

    /**
     * Create a new conversation.  Parameters ---------- create_conversation : ConversationModel     Conversation information to create. user : dict     Authenticated user information.
     * Create Conversation
     * @param param the request object
     */
    public createConversationApiV1SecureConversationsPostWithHttpInfo(param: ConversationsApiCreateConversationApiV1SecureConversationsPostRequest, options?: Configuration): Promise<HttpInfo<any>> {
        return this.api.createConversationApiV1SecureConversationsPostWithHttpInfo(param.conversationModel,  options).toPromise();
    }

    /**
     * Create a new conversation.  Parameters ---------- create_conversation : ConversationModel     Conversation information to create. user : dict     Authenticated user information.
     * Create Conversation
     * @param param the request object
     */
    public createConversationApiV1SecureConversationsPost(param: ConversationsApiCreateConversationApiV1SecureConversationsPostRequest, options?: Configuration): Promise<any> {
        return this.api.createConversationApiV1SecureConversationsPost(param.conversationModel,  options).toPromise();
    }

    /**
     * Delete Conversation
     * @param param the request object
     */
    public deleteConversationApiV1SecureConversationsCidDeleteWithHttpInfo(param: ConversationsApiDeleteConversationApiV1SecureConversationsCidDeleteRequest, options?: Configuration): Promise<HttpInfo<any>> {
        return this.api.deleteConversationApiV1SecureConversationsCidDeleteWithHttpInfo(param.cid,  options).toPromise();
    }

    /**
     * Delete Conversation
     * @param param the request object
     */
    public deleteConversationApiV1SecureConversationsCidDelete(param: ConversationsApiDeleteConversationApiV1SecureConversationsCidDeleteRequest, options?: Configuration): Promise<any> {
        return this.api.deleteConversationApiV1SecureConversationsCidDelete(param.cid,  options).toPromise();
    }

    /**
     * Get all conversations for the authenticated user.  Returns ------- dict     A dictionary containing all conversations for the user.
     * Get All Conversations
     * @param param the request object
     */
    public getAllConversationsApiV1SecureConversationsAllGetWithHttpInfo(param: ConversationsApiGetAllConversationsApiV1SecureConversationsAllGetRequest = {}, options?: Configuration): Promise<HttpInfo<ConversationResponse>> {
        return this.api.getAllConversationsApiV1SecureConversationsAllGetWithHttpInfo( options).toPromise();
    }

    /**
     * Get all conversations for the authenticated user.  Returns ------- dict     A dictionary containing all conversations for the user.
     * Get All Conversations
     * @param param the request object
     */
    public getAllConversationsApiV1SecureConversationsAllGet(param: ConversationsApiGetAllConversationsApiV1SecureConversationsAllGetRequest = {}, options?: Configuration): Promise<ConversationResponse> {
        return this.api.getAllConversationsApiV1SecureConversationsAllGet( options).toPromise();
    }

    /**
     * Get a conversation by ID.  Returns ------- dict     A dictionary containing the conversation details.
     * Get Conversation
     * @param param the request object
     */
    public getConversationApiV1SecureConversationsCidGetWithHttpInfo(param: ConversationsApiGetConversationApiV1SecureConversationsCidGetRequest, options?: Configuration): Promise<HttpInfo<ResponseMessage>> {
        return this.api.getConversationApiV1SecureConversationsCidGetWithHttpInfo(param.cid,  options).toPromise();
    }

    /**
     * Get a conversation by ID.  Returns ------- dict     A dictionary containing the conversation details.
     * Get Conversation
     * @param param the request object
     */
    public getConversationApiV1SecureConversationsCidGet(param: ConversationsApiGetConversationApiV1SecureConversationsCidGetRequest, options?: Configuration): Promise<ResponseMessage> {
        return this.api.getConversationApiV1SecureConversationsCidGet(param.cid,  options).toPromise();
    }

    /**
     * Update a conversation.  Parameters ---------- update_conversation : ConversationModel     Conversation update information. user : dict     Authenticated user information.
     * Update Conversation
     * @param param the request object
     */
    public updateConversationApiV1SecureConversationsPutWithHttpInfo(param: ConversationsApiUpdateConversationApiV1SecureConversationsPutRequest, options?: Configuration): Promise<HttpInfo<any>> {
        return this.api.updateConversationApiV1SecureConversationsPutWithHttpInfo(param.conversationModel,  options).toPromise();
    }

    /**
     * Update a conversation.  Parameters ---------- update_conversation : ConversationModel     Conversation update information. user : dict     Authenticated user information.
     * Update Conversation
     * @param param the request object
     */
    public updateConversationApiV1SecureConversationsPut(param: ConversationsApiUpdateConversationApiV1SecureConversationsPutRequest, options?: Configuration): Promise<any> {
        return this.api.updateConversationApiV1SecureConversationsPut(param.conversationModel,  options).toPromise();
    }

}

import { ObservableDefaultApi } from "./ObservableAPI";
import { DefaultApiRequestFactory, DefaultApiResponseProcessor} from "../apis/DefaultApi";

export interface DefaultApiGetTestrouteApiV1PublicGetRequest {
}

export class ObjectDefaultApi {
    private api: ObservableDefaultApi

    public constructor(configuration: Configuration, requestFactory?: DefaultApiRequestFactory, responseProcessor?: DefaultApiResponseProcessor) {
        this.api = new ObservableDefaultApi(configuration, requestFactory, responseProcessor);
    }

    /**
     * This endpoint is used to check if the database connection is healthy.  Returns ------- dict     A dictionary containing the status of the database connection.     - If the connection is healthy, the dictionary will contain     {\"detail\": \"OK\"}.     - If the connection is not healthy, the dictionary will contain     {\"detail\": \"DB conn failed\"}.
     * Get Testroute
     * @param param the request object
     */
    public getTestrouteApiV1PublicGetWithHttpInfo(param: DefaultApiGetTestrouteApiV1PublicGetRequest = {}, options?: Configuration): Promise<HttpInfo<any>> {
        return this.api.getTestrouteApiV1PublicGetWithHttpInfo( options).toPromise();
    }

    /**
     * This endpoint is used to check if the database connection is healthy.  Returns ------- dict     A dictionary containing the status of the database connection.     - If the connection is healthy, the dictionary will contain     {\"detail\": \"OK\"}.     - If the connection is not healthy, the dictionary will contain     {\"detail\": \"DB conn failed\"}.
     * Get Testroute
     * @param param the request object
     */
    public getTestrouteApiV1PublicGet(param: DefaultApiGetTestrouteApiV1PublicGetRequest = {}, options?: Configuration): Promise<any> {
        return this.api.getTestrouteApiV1PublicGet( options).toPromise();
    }

}

import { ObservableUserApi } from "./ObservableAPI";
import { UserApiRequestFactory, UserApiResponseProcessor} from "../apis/UserApi";

export interface UserApiCreateUserprofileApiV1SecureUsersProfilePostRequest {
    /**
     * 
     * @type UserProfile
     * @memberof UserApicreateUserprofileApiV1SecureUsersProfilePost
     */
    userProfile: UserProfile
}

export interface UserApiDeleteUserprofileApiV1SecureUsersProfileDeleteRequest {
}

export interface UserApiGetTestrouteApiV1SecureGetRequest {
}

export interface UserApiGetUserauthApiV1SecureUsersAuthPostRequest {
    /**
     * 
     * @type UserProfile
     * @memberof UserApigetUserauthApiV1SecureUsersAuthPost
     */
    userProfile: UserProfile
}

export interface UserApiGetUserprofileApiV1SecureUsersProfileGetRequest {
}

export interface UserApiGetUserroleApiV1SecureUsersRoleGetRequest {
}

export interface UserApiUpdateUserprofileApiV1SecureUsersProfilePutRequest {
    /**
     * 
     * @type UserProfile
     * @memberof UserApiupdateUserprofileApiV1SecureUsersProfilePut
     */
    userProfile: UserProfile
}

export interface UserApiUpdateUsertokenApiV1SecureUsersRenewPutRequest {
}

export class ObjectUserApi {
    private api: ObservableUserApi

    public constructor(configuration: Configuration, requestFactory?: UserApiRequestFactory, responseProcessor?: UserApiResponseProcessor) {
        this.api = new ObservableUserApi(configuration, requestFactory, responseProcessor);
    }

    /**
     * Create a new user profile.  Parameters ---------- user_profile : UserProfile     User profile information. user : dict     Authenticated user information.
     * Create Userprofile
     * @param param the request object
     */
    public createUserprofileApiV1SecureUsersProfilePostWithHttpInfo(param: UserApiCreateUserprofileApiV1SecureUsersProfilePostRequest, options?: Configuration): Promise<HttpInfo<ResponseMessage>> {
        return this.api.createUserprofileApiV1SecureUsersProfilePostWithHttpInfo(param.userProfile,  options).toPromise();
    }

    /**
     * Create a new user profile.  Parameters ---------- user_profile : UserProfile     User profile information. user : dict     Authenticated user information.
     * Create Userprofile
     * @param param the request object
     */
    public createUserprofileApiV1SecureUsersProfilePost(param: UserApiCreateUserprofileApiV1SecureUsersProfilePostRequest, options?: Configuration): Promise<ResponseMessage> {
        return this.api.createUserprofileApiV1SecureUsersProfilePost(param.userProfile,  options).toPromise();
    }

    /**
     * Delete Userprofile
     * @param param the request object
     */
    public deleteUserprofileApiV1SecureUsersProfileDeleteWithHttpInfo(param: UserApiDeleteUserprofileApiV1SecureUsersProfileDeleteRequest = {}, options?: Configuration): Promise<HttpInfo<any>> {
        return this.api.deleteUserprofileApiV1SecureUsersProfileDeleteWithHttpInfo( options).toPromise();
    }

    /**
     * Delete Userprofile
     * @param param the request object
     */
    public deleteUserprofileApiV1SecureUsersProfileDelete(param: UserApiDeleteUserprofileApiV1SecureUsersProfileDeleteRequest = {}, options?: Configuration): Promise<any> {
        return this.api.deleteUserprofileApiV1SecureUsersProfileDelete( options).toPromise();
    }

    /**
     * This endpoint returns information about the currently authenticated user.  Parameters ---------- user : dict     A dictionary containing user information retrieved     from the `get_user` dependency from `auth` module.     The dictionary is expected to have the following structure:     ```     {         \'id\': <user_id>,         \'email\': <user_email>,         \'role\': <user_role>     }     ```  Returns ------- ResponseMessage     `detail` is `UserResponseMessage` containing the user\'s id, email, and role.
     * Get Testroute
     * @param param the request object
     */
    public getTestrouteApiV1SecureGetWithHttpInfo(param: UserApiGetTestrouteApiV1SecureGetRequest = {}, options?: Configuration): Promise<HttpInfo<ResponseMessage>> {
        return this.api.getTestrouteApiV1SecureGetWithHttpInfo( options).toPromise();
    }

    /**
     * This endpoint returns information about the currently authenticated user.  Parameters ---------- user : dict     A dictionary containing user information retrieved     from the `get_user` dependency from `auth` module.     The dictionary is expected to have the following structure:     ```     {         \'id\': <user_id>,         \'email\': <user_email>,         \'role\': <user_role>     }     ```  Returns ------- ResponseMessage     `detail` is `UserResponseMessage` containing the user\'s id, email, and role.
     * Get Testroute
     * @param param the request object
     */
    public getTestrouteApiV1SecureGet(param: UserApiGetTestrouteApiV1SecureGetRequest = {}, options?: Configuration): Promise<ResponseMessage> {
        return this.api.getTestrouteApiV1SecureGet( options).toPromise();
    }

    /**
     * Get Userauth
     * @param param the request object
     */
    public getUserauthApiV1SecureUsersAuthPostWithHttpInfo(param: UserApiGetUserauthApiV1SecureUsersAuthPostRequest, options?: Configuration): Promise<HttpInfo<ResponseMessage>> {
        return this.api.getUserauthApiV1SecureUsersAuthPostWithHttpInfo(param.userProfile,  options).toPromise();
    }

    /**
     * Get Userauth
     * @param param the request object
     */
    public getUserauthApiV1SecureUsersAuthPost(param: UserApiGetUserauthApiV1SecureUsersAuthPostRequest, options?: Configuration): Promise<ResponseMessage> {
        return this.api.getUserauthApiV1SecureUsersAuthPost(param.userProfile,  options).toPromise();
    }

    /**
     * This endpoint returns information about the currently authenticated user.  Parameters ---------- user : dict     A dictionary containing user information retrieved     from the `get_user` dependency from `auth` module.     The dictionary is expected     to have the following structure:     ```     {         \'id\': <user_id>,         \'email\': <user_email>,         \'role\': <user_role>     }     ```  Returns ------- ResponseMessage     `detail` is `UserResponseMessage` containing the user\'s id, email, and role.
     * Get Userprofile
     * @param param the request object
     */
    public getUserprofileApiV1SecureUsersProfileGetWithHttpInfo(param: UserApiGetUserprofileApiV1SecureUsersProfileGetRequest = {}, options?: Configuration): Promise<HttpInfo<ResponseMessage>> {
        return this.api.getUserprofileApiV1SecureUsersProfileGetWithHttpInfo( options).toPromise();
    }

    /**
     * This endpoint returns information about the currently authenticated user.  Parameters ---------- user : dict     A dictionary containing user information retrieved     from the `get_user` dependency from `auth` module.     The dictionary is expected     to have the following structure:     ```     {         \'id\': <user_id>,         \'email\': <user_email>,         \'role\': <user_role>     }     ```  Returns ------- ResponseMessage     `detail` is `UserResponseMessage` containing the user\'s id, email, and role.
     * Get Userprofile
     * @param param the request object
     */
    public getUserprofileApiV1SecureUsersProfileGet(param: UserApiGetUserprofileApiV1SecureUsersProfileGetRequest = {}, options?: Configuration): Promise<ResponseMessage> {
        return this.api.getUserprofileApiV1SecureUsersProfileGet( options).toPromise();
    }

    /**
     * This endpoint returns the role of the currently authenticated user.  Parameters ---------- user : dict     A dictionary containing user information retrieved     from the `get_user` dependency from `auth` module.     The dictionary is expected to have the following structure:     ```     {         \'id\': <user_id>,         \'email\': <user_email>,         \'role\': <user_role>     }  Returns ------- ResponseMessage     `detail` string of the user\'s role.
     * Get Userrole
     * @param param the request object
     */
    public getUserroleApiV1SecureUsersRoleGetWithHttpInfo(param: UserApiGetUserroleApiV1SecureUsersRoleGetRequest = {}, options?: Configuration): Promise<HttpInfo<ResponseMessage>> {
        return this.api.getUserroleApiV1SecureUsersRoleGetWithHttpInfo( options).toPromise();
    }

    /**
     * This endpoint returns the role of the currently authenticated user.  Parameters ---------- user : dict     A dictionary containing user information retrieved     from the `get_user` dependency from `auth` module.     The dictionary is expected to have the following structure:     ```     {         \'id\': <user_id>,         \'email\': <user_email>,         \'role\': <user_role>     }  Returns ------- ResponseMessage     `detail` string of the user\'s role.
     * Get Userrole
     * @param param the request object
     */
    public getUserroleApiV1SecureUsersRoleGet(param: UserApiGetUserroleApiV1SecureUsersRoleGetRequest = {}, options?: Configuration): Promise<ResponseMessage> {
        return this.api.getUserroleApiV1SecureUsersRoleGet( options).toPromise();
    }

    /**
     * Update the authenticated user\'s profile.  Parameters ---------- update_user : UpdateUserProfile     User profile information to update. user : dict     Authenticated user information.
     * Update Userprofile
     * @param param the request object
     */
    public updateUserprofileApiV1SecureUsersProfilePutWithHttpInfo(param: UserApiUpdateUserprofileApiV1SecureUsersProfilePutRequest, options?: Configuration): Promise<HttpInfo<any>> {
        return this.api.updateUserprofileApiV1SecureUsersProfilePutWithHttpInfo(param.userProfile,  options).toPromise();
    }

    /**
     * Update the authenticated user\'s profile.  Parameters ---------- update_user : UpdateUserProfile     User profile information to update. user : dict     Authenticated user information.
     * Update Userprofile
     * @param param the request object
     */
    public updateUserprofileApiV1SecureUsersProfilePut(param: UserApiUpdateUserprofileApiV1SecureUsersProfilePutRequest, options?: Configuration): Promise<any> {
        return this.api.updateUserprofileApiV1SecureUsersProfilePut(param.userProfile,  options).toPromise();
    }

    /**
     * Updates the API key for the currently authenticated user.  Parameters ---------- user : dict     A dictionary containing user information retrieved     from the `get_user` dependency from `auth` module.     The dictionary is expected     to have the following structure:     ```     {         \'id\': <user_id>,         \'email\': <user_email>,         \'role\': <user_role>     }     ```  Returns ------- ResponseMessage     `detail` is the string of the new API key.
     * Update Usertoken
     * @param param the request object
     */
    public updateUsertokenApiV1SecureUsersRenewPutWithHttpInfo(param: UserApiUpdateUsertokenApiV1SecureUsersRenewPutRequest = {}, options?: Configuration): Promise<HttpInfo<ResponseMessage>> {
        return this.api.updateUsertokenApiV1SecureUsersRenewPutWithHttpInfo( options).toPromise();
    }

    /**
     * Updates the API key for the currently authenticated user.  Parameters ---------- user : dict     A dictionary containing user information retrieved     from the `get_user` dependency from `auth` module.     The dictionary is expected     to have the following structure:     ```     {         \'id\': <user_id>,         \'email\': <user_email>,         \'role\': <user_role>     }     ```  Returns ------- ResponseMessage     `detail` is the string of the new API key.
     * Update Usertoken
     * @param param the request object
     */
    public updateUsertokenApiV1SecureUsersRenewPut(param: UserApiUpdateUsertokenApiV1SecureUsersRenewPutRequest = {}, options?: Configuration): Promise<ResponseMessage> {
        return this.api.updateUsertokenApiV1SecureUsersRenewPut( options).toPromise();
    }

}
