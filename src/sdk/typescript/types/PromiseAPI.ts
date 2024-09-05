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
import { ObservableAPIKeysApi } from './ObservableAPI';

import { APIKeysApiRequestFactory, APIKeysApiResponseProcessor} from "../apis/APIKeysApi";
export class PromiseAPIKeysApi {
    private api: ObservableAPIKeysApi

    public constructor(
        configuration: Configuration,
        requestFactory?: APIKeysApiRequestFactory,
        responseProcessor?: APIKeysApiResponseProcessor
    ) {
        this.api = new ObservableAPIKeysApi(configuration, requestFactory, responseProcessor);
    }

    /**
     * Updates the API key for the currently authenticated user.  Parameters ---------- user : dict     A dictionary containing user information retrieved     from the `get_user` dependency from `auth` module.     The dictionary is expected     to have the following structure:     ```     {         \'id\': <user_id>,         \'email\': <user_email>,         \'role\': <user_role>     }     ```  Returns ------- ResponseMessage     `detail` is the string of the new API key.
     * Update Usertoken
     */
    public updateUsertokenApiV1SecureUsersRenewPutWithHttpInfo(_options?: Configuration): Promise<HttpInfo<ResponseMessage>> {
        const result = this.api.updateUsertokenApiV1SecureUsersRenewPutWithHttpInfo(_options);
        return result.toPromise();
    }

    /**
     * Updates the API key for the currently authenticated user.  Parameters ---------- user : dict     A dictionary containing user information retrieved     from the `get_user` dependency from `auth` module.     The dictionary is expected     to have the following structure:     ```     {         \'id\': <user_id>,         \'email\': <user_email>,         \'role\': <user_role>     }     ```  Returns ------- ResponseMessage     `detail` is the string of the new API key.
     * Update Usertoken
     */
    public updateUsertokenApiV1SecureUsersRenewPut(_options?: Configuration): Promise<ResponseMessage> {
        const result = this.api.updateUsertokenApiV1SecureUsersRenewPut(_options);
        return result.toPromise();
    }


}



import { ObservableCommentsApi } from './ObservableAPI';

import { CommentsApiRequestFactory, CommentsApiResponseProcessor} from "../apis/CommentsApi";
export class PromiseCommentsApi {
    private api: ObservableCommentsApi

    public constructor(
        configuration: Configuration,
        requestFactory?: CommentsApiRequestFactory,
        responseProcessor?: CommentsApiResponseProcessor
    ) {
        this.api = new ObservableCommentsApi(configuration, requestFactory, responseProcessor);
    }

    /**
     * Create a new comment.
     * Create Comment
     * @param commentModel 
     */
    public createCommentApiV1SecureCommentsPostWithHttpInfo(commentModel: CommentModel, _options?: Configuration): Promise<HttpInfo<any>> {
        const result = this.api.createCommentApiV1SecureCommentsPostWithHttpInfo(commentModel, _options);
        return result.toPromise();
    }

    /**
     * Create a new comment.
     * Create Comment
     * @param commentModel 
     */
    public createCommentApiV1SecureCommentsPost(commentModel: CommentModel, _options?: Configuration): Promise<any> {
        const result = this.api.createCommentApiV1SecureCommentsPost(commentModel, _options);
        return result.toPromise();
    }

    /**
     * Delete Comment
     * @param cid 
     */
    public deleteCommentApiV1SecureCommentsCidDeleteWithHttpInfo(cid: number, _options?: Configuration): Promise<HttpInfo<any>> {
        const result = this.api.deleteCommentApiV1SecureCommentsCidDeleteWithHttpInfo(cid, _options);
        return result.toPromise();
    }

    /**
     * Delete Comment
     * @param cid 
     */
    public deleteCommentApiV1SecureCommentsCidDelete(cid: number, _options?: Configuration): Promise<any> {
        const result = this.api.deleteCommentApiV1SecureCommentsCidDelete(cid, _options);
        return result.toPromise();
    }

    /**
     * Get Comments
     * @param cid 
     * @param random 
     * @param moderated 
     */
    public getCommentsApiV1SecureCommentsCidGetWithHttpInfo(cid: number, random?: boolean, moderated?: boolean, _options?: Configuration): Promise<HttpInfo<CommentResponse>> {
        const result = this.api.getCommentsApiV1SecureCommentsCidGetWithHttpInfo(cid, random, moderated, _options);
        return result.toPromise();
    }

    /**
     * Get Comments
     * @param cid 
     * @param random 
     * @param moderated 
     */
    public getCommentsApiV1SecureCommentsCidGet(cid: number, random?: boolean, moderated?: boolean, _options?: Configuration): Promise<CommentResponse> {
        const result = this.api.getCommentsApiV1SecureCommentsCidGet(cid, random, moderated, _options);
        return result.toPromise();
    }

    /**
     * Get comments waiting for moderation from a conversation.  Returns ------- dict     A dictionary containing comments waiting for moderation.
     * Get Comments For Moderation
     * @param cid 
     */
    public getCommentsForModerationApiV1SecureCommentsCidModerateGetWithHttpInfo(cid: number, _options?: Configuration): Promise<HttpInfo<CommentResponse>> {
        const result = this.api.getCommentsForModerationApiV1SecureCommentsCidModerateGetWithHttpInfo(cid, _options);
        return result.toPromise();
    }

    /**
     * Get comments waiting for moderation from a conversation.  Returns ------- dict     A dictionary containing comments waiting for moderation.
     * Get Comments For Moderation
     * @param cid 
     */
    public getCommentsForModerationApiV1SecureCommentsCidModerateGet(cid: number, _options?: Configuration): Promise<CommentResponse> {
        const result = this.api.getCommentsForModerationApiV1SecureCommentsCidModerateGet(cid, _options);
        return result.toPromise();
    }

    /**
     * Update a comment.
     * Update Comment
     * @param commentModel 
     */
    public updateCommentApiV1SecureCommentsPutWithHttpInfo(commentModel: CommentModel, _options?: Configuration): Promise<HttpInfo<any>> {
        const result = this.api.updateCommentApiV1SecureCommentsPutWithHttpInfo(commentModel, _options);
        return result.toPromise();
    }

    /**
     * Update a comment.
     * Update Comment
     * @param commentModel 
     */
    public updateCommentApiV1SecureCommentsPut(commentModel: CommentModel, _options?: Configuration): Promise<any> {
        const result = this.api.updateCommentApiV1SecureCommentsPut(commentModel, _options);
        return result.toPromise();
    }


}



import { ObservableConversationsApi } from './ObservableAPI';

import { ConversationsApiRequestFactory, ConversationsApiResponseProcessor} from "../apis/ConversationsApi";
export class PromiseConversationsApi {
    private api: ObservableConversationsApi

    public constructor(
        configuration: Configuration,
        requestFactory?: ConversationsApiRequestFactory,
        responseProcessor?: ConversationsApiResponseProcessor
    ) {
        this.api = new ObservableConversationsApi(configuration, requestFactory, responseProcessor);
    }

    /**
     * Create a new conversation.  Parameters ---------- create_conversation : ConversationModel     Conversation information to create. user : dict     Authenticated user information.
     * Create Conversation
     * @param conversationModel 
     */
    public createConversationApiV1SecureConversationsPostWithHttpInfo(conversationModel: ConversationModel, _options?: Configuration): Promise<HttpInfo<any>> {
        const result = this.api.createConversationApiV1SecureConversationsPostWithHttpInfo(conversationModel, _options);
        return result.toPromise();
    }

    /**
     * Create a new conversation.  Parameters ---------- create_conversation : ConversationModel     Conversation information to create. user : dict     Authenticated user information.
     * Create Conversation
     * @param conversationModel 
     */
    public createConversationApiV1SecureConversationsPost(conversationModel: ConversationModel, _options?: Configuration): Promise<any> {
        const result = this.api.createConversationApiV1SecureConversationsPost(conversationModel, _options);
        return result.toPromise();
    }

    /**
     * Delete Conversation
     * @param cid 
     */
    public deleteConversationApiV1SecureConversationsCidDeleteWithHttpInfo(cid: number, _options?: Configuration): Promise<HttpInfo<any>> {
        const result = this.api.deleteConversationApiV1SecureConversationsCidDeleteWithHttpInfo(cid, _options);
        return result.toPromise();
    }

    /**
     * Delete Conversation
     * @param cid 
     */
    public deleteConversationApiV1SecureConversationsCidDelete(cid: number, _options?: Configuration): Promise<any> {
        const result = this.api.deleteConversationApiV1SecureConversationsCidDelete(cid, _options);
        return result.toPromise();
    }

    /**
     * Get all conversations for the authenticated user.  Returns ------- dict     A dictionary containing all conversations for the user.
     * Get All Conversations
     */
    public getAllConversationsApiV1SecureConversationsAllGetWithHttpInfo(_options?: Configuration): Promise<HttpInfo<ConversationResponse>> {
        const result = this.api.getAllConversationsApiV1SecureConversationsAllGetWithHttpInfo(_options);
        return result.toPromise();
    }

    /**
     * Get all conversations for the authenticated user.  Returns ------- dict     A dictionary containing all conversations for the user.
     * Get All Conversations
     */
    public getAllConversationsApiV1SecureConversationsAllGet(_options?: Configuration): Promise<ConversationResponse> {
        const result = this.api.getAllConversationsApiV1SecureConversationsAllGet(_options);
        return result.toPromise();
    }

    /**
     * Get a conversation by ID.  Returns ------- dict     A dictionary containing the conversation details.
     * Get Conversation
     * @param cid 
     */
    public getConversationApiV1SecureConversationsCidGetWithHttpInfo(cid: number, _options?: Configuration): Promise<HttpInfo<ResponseMessage>> {
        const result = this.api.getConversationApiV1SecureConversationsCidGetWithHttpInfo(cid, _options);
        return result.toPromise();
    }

    /**
     * Get a conversation by ID.  Returns ------- dict     A dictionary containing the conversation details.
     * Get Conversation
     * @param cid 
     */
    public getConversationApiV1SecureConversationsCidGet(cid: number, _options?: Configuration): Promise<ResponseMessage> {
        const result = this.api.getConversationApiV1SecureConversationsCidGet(cid, _options);
        return result.toPromise();
    }

    /**
     * Update a conversation.  Parameters ---------- update_conversation : ConversationModel     Conversation update information. user : dict     Authenticated user information.
     * Update Conversation
     * @param conversationModel 
     */
    public updateConversationApiV1SecureConversationsPutWithHttpInfo(conversationModel: ConversationModel, _options?: Configuration): Promise<HttpInfo<any>> {
        const result = this.api.updateConversationApiV1SecureConversationsPutWithHttpInfo(conversationModel, _options);
        return result.toPromise();
    }

    /**
     * Update a conversation.  Parameters ---------- update_conversation : ConversationModel     Conversation update information. user : dict     Authenticated user information.
     * Update Conversation
     * @param conversationModel 
     */
    public updateConversationApiV1SecureConversationsPut(conversationModel: ConversationModel, _options?: Configuration): Promise<any> {
        const result = this.api.updateConversationApiV1SecureConversationsPut(conversationModel, _options);
        return result.toPromise();
    }


}



import { ObservableDefaultApi } from './ObservableAPI';

import { DefaultApiRequestFactory, DefaultApiResponseProcessor} from "../apis/DefaultApi";
export class PromiseDefaultApi {
    private api: ObservableDefaultApi

    public constructor(
        configuration: Configuration,
        requestFactory?: DefaultApiRequestFactory,
        responseProcessor?: DefaultApiResponseProcessor
    ) {
        this.api = new ObservableDefaultApi(configuration, requestFactory, responseProcessor);
    }

    /**
     * This endpoint is used to check if the database connection is healthy.  Returns ------- dict     A dictionary containing the status of the database connection.     - If the connection is healthy, the dictionary will contain     {\"detail\": \"OK\"}.     - If the connection is not healthy, the dictionary will contain     {\"detail\": \"DB conn failed\"}.
     * Get Testroute
     */
    public getTestrouteApiV1PublicGetWithHttpInfo(_options?: Configuration): Promise<HttpInfo<any>> {
        const result = this.api.getTestrouteApiV1PublicGetWithHttpInfo(_options);
        return result.toPromise();
    }

    /**
     * This endpoint is used to check if the database connection is healthy.  Returns ------- dict     A dictionary containing the status of the database connection.     - If the connection is healthy, the dictionary will contain     {\"detail\": \"OK\"}.     - If the connection is not healthy, the dictionary will contain     {\"detail\": \"DB conn failed\"}.
     * Get Testroute
     */
    public getTestrouteApiV1PublicGet(_options?: Configuration): Promise<any> {
        const result = this.api.getTestrouteApiV1PublicGet(_options);
        return result.toPromise();
    }


}



import { ObservableUserApi } from './ObservableAPI';

import { UserApiRequestFactory, UserApiResponseProcessor} from "../apis/UserApi";
export class PromiseUserApi {
    private api: ObservableUserApi

    public constructor(
        configuration: Configuration,
        requestFactory?: UserApiRequestFactory,
        responseProcessor?: UserApiResponseProcessor
    ) {
        this.api = new ObservableUserApi(configuration, requestFactory, responseProcessor);
    }

    /**
     * Create a new user profile.  Parameters ---------- user_profile : UserProfile     User profile information. user : dict     Authenticated user information.
     * Create Userprofile
     * @param userProfile 
     */
    public createUserprofileApiV1SecureUsersProfilePostWithHttpInfo(userProfile: UserProfile, _options?: Configuration): Promise<HttpInfo<ResponseMessage>> {
        const result = this.api.createUserprofileApiV1SecureUsersProfilePostWithHttpInfo(userProfile, _options);
        return result.toPromise();
    }

    /**
     * Create a new user profile.  Parameters ---------- user_profile : UserProfile     User profile information. user : dict     Authenticated user information.
     * Create Userprofile
     * @param userProfile 
     */
    public createUserprofileApiV1SecureUsersProfilePost(userProfile: UserProfile, _options?: Configuration): Promise<ResponseMessage> {
        const result = this.api.createUserprofileApiV1SecureUsersProfilePost(userProfile, _options);
        return result.toPromise();
    }

    /**
     * Delete Userprofile
     */
    public deleteUserprofileApiV1SecureUsersProfileDeleteWithHttpInfo(_options?: Configuration): Promise<HttpInfo<any>> {
        const result = this.api.deleteUserprofileApiV1SecureUsersProfileDeleteWithHttpInfo(_options);
        return result.toPromise();
    }

    /**
     * Delete Userprofile
     */
    public deleteUserprofileApiV1SecureUsersProfileDelete(_options?: Configuration): Promise<any> {
        const result = this.api.deleteUserprofileApiV1SecureUsersProfileDelete(_options);
        return result.toPromise();
    }

    /**
     * This endpoint returns information about the currently authenticated user.  Parameters ---------- user : dict     A dictionary containing user information retrieved     from the `get_user` dependency from `auth` module.     The dictionary is expected to have the following structure:     ```     {         \'id\': <user_id>,         \'email\': <user_email>,         \'role\': <user_role>     }     ```  Returns ------- ResponseMessage     `detail` is `UserResponseMessage` containing the user\'s id, email, and role.
     * Get Testroute
     */
    public getTestrouteApiV1SecureGetWithHttpInfo(_options?: Configuration): Promise<HttpInfo<ResponseMessage>> {
        const result = this.api.getTestrouteApiV1SecureGetWithHttpInfo(_options);
        return result.toPromise();
    }

    /**
     * This endpoint returns information about the currently authenticated user.  Parameters ---------- user : dict     A dictionary containing user information retrieved     from the `get_user` dependency from `auth` module.     The dictionary is expected to have the following structure:     ```     {         \'id\': <user_id>,         \'email\': <user_email>,         \'role\': <user_role>     }     ```  Returns ------- ResponseMessage     `detail` is `UserResponseMessage` containing the user\'s id, email, and role.
     * Get Testroute
     */
    public getTestrouteApiV1SecureGet(_options?: Configuration): Promise<ResponseMessage> {
        const result = this.api.getTestrouteApiV1SecureGet(_options);
        return result.toPromise();
    }

    /**
     * Get Userauth
     * @param userProfile 
     */
    public getUserauthApiV1SecureUsersAuthPostWithHttpInfo(userProfile: UserProfile, _options?: Configuration): Promise<HttpInfo<ResponseMessage>> {
        const result = this.api.getUserauthApiV1SecureUsersAuthPostWithHttpInfo(userProfile, _options);
        return result.toPromise();
    }

    /**
     * Get Userauth
     * @param userProfile 
     */
    public getUserauthApiV1SecureUsersAuthPost(userProfile: UserProfile, _options?: Configuration): Promise<ResponseMessage> {
        const result = this.api.getUserauthApiV1SecureUsersAuthPost(userProfile, _options);
        return result.toPromise();
    }

    /**
     * This endpoint returns information about the currently authenticated user.  Parameters ---------- user : dict     A dictionary containing user information retrieved     from the `get_user` dependency from `auth` module.     The dictionary is expected     to have the following structure:     ```     {         \'id\': <user_id>,         \'email\': <user_email>,         \'role\': <user_role>     }     ```  Returns ------- ResponseMessage     `detail` is `UserResponseMessage` containing the user\'s id, email, and role.
     * Get Userprofile
     */
    public getUserprofileApiV1SecureUsersProfileGetWithHttpInfo(_options?: Configuration): Promise<HttpInfo<ResponseMessage>> {
        const result = this.api.getUserprofileApiV1SecureUsersProfileGetWithHttpInfo(_options);
        return result.toPromise();
    }

    /**
     * This endpoint returns information about the currently authenticated user.  Parameters ---------- user : dict     A dictionary containing user information retrieved     from the `get_user` dependency from `auth` module.     The dictionary is expected     to have the following structure:     ```     {         \'id\': <user_id>,         \'email\': <user_email>,         \'role\': <user_role>     }     ```  Returns ------- ResponseMessage     `detail` is `UserResponseMessage` containing the user\'s id, email, and role.
     * Get Userprofile
     */
    public getUserprofileApiV1SecureUsersProfileGet(_options?: Configuration): Promise<ResponseMessage> {
        const result = this.api.getUserprofileApiV1SecureUsersProfileGet(_options);
        return result.toPromise();
    }

    /**
     * This endpoint returns the role of the currently authenticated user.  Parameters ---------- user : dict     A dictionary containing user information retrieved     from the `get_user` dependency from `auth` module.     The dictionary is expected to have the following structure:     ```     {         \'id\': <user_id>,         \'email\': <user_email>,         \'role\': <user_role>     }  Returns ------- ResponseMessage     `detail` string of the user\'s role.
     * Get Userrole
     */
    public getUserroleApiV1SecureUsersRoleGetWithHttpInfo(_options?: Configuration): Promise<HttpInfo<ResponseMessage>> {
        const result = this.api.getUserroleApiV1SecureUsersRoleGetWithHttpInfo(_options);
        return result.toPromise();
    }

    /**
     * This endpoint returns the role of the currently authenticated user.  Parameters ---------- user : dict     A dictionary containing user information retrieved     from the `get_user` dependency from `auth` module.     The dictionary is expected to have the following structure:     ```     {         \'id\': <user_id>,         \'email\': <user_email>,         \'role\': <user_role>     }  Returns ------- ResponseMessage     `detail` string of the user\'s role.
     * Get Userrole
     */
    public getUserroleApiV1SecureUsersRoleGet(_options?: Configuration): Promise<ResponseMessage> {
        const result = this.api.getUserroleApiV1SecureUsersRoleGet(_options);
        return result.toPromise();
    }

    /**
     * Update the authenticated user\'s profile.  Parameters ---------- update_user : UpdateUserProfile     User profile information to update. user : dict     Authenticated user information.
     * Update Userprofile
     * @param userProfile 
     */
    public updateUserprofileApiV1SecureUsersProfilePutWithHttpInfo(userProfile: UserProfile, _options?: Configuration): Promise<HttpInfo<any>> {
        const result = this.api.updateUserprofileApiV1SecureUsersProfilePutWithHttpInfo(userProfile, _options);
        return result.toPromise();
    }

    /**
     * Update the authenticated user\'s profile.  Parameters ---------- update_user : UpdateUserProfile     User profile information to update. user : dict     Authenticated user information.
     * Update Userprofile
     * @param userProfile 
     */
    public updateUserprofileApiV1SecureUsersProfilePut(userProfile: UserProfile, _options?: Configuration): Promise<any> {
        const result = this.api.updateUserprofileApiV1SecureUsersProfilePut(userProfile, _options);
        return result.toPromise();
    }

    /**
     * Updates the API key for the currently authenticated user.  Parameters ---------- user : dict     A dictionary containing user information retrieved     from the `get_user` dependency from `auth` module.     The dictionary is expected     to have the following structure:     ```     {         \'id\': <user_id>,         \'email\': <user_email>,         \'role\': <user_role>     }     ```  Returns ------- ResponseMessage     `detail` is the string of the new API key.
     * Update Usertoken
     */
    public updateUsertokenApiV1SecureUsersRenewPutWithHttpInfo(_options?: Configuration): Promise<HttpInfo<ResponseMessage>> {
        const result = this.api.updateUsertokenApiV1SecureUsersRenewPutWithHttpInfo(_options);
        return result.toPromise();
    }

    /**
     * Updates the API key for the currently authenticated user.  Parameters ---------- user : dict     A dictionary containing user information retrieved     from the `get_user` dependency from `auth` module.     The dictionary is expected     to have the following structure:     ```     {         \'id\': <user_id>,         \'email\': <user_email>,         \'role\': <user_role>     }     ```  Returns ------- ResponseMessage     `detail` is the string of the new API key.
     * Update Usertoken
     */
    public updateUsertokenApiV1SecureUsersRenewPut(_options?: Configuration): Promise<ResponseMessage> {
        const result = this.api.updateUsertokenApiV1SecureUsersRenewPut(_options);
        return result.toPromise();
    }


}



