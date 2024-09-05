import { ResponseContext, RequestContext, HttpFile, HttpInfo } from '../http/http';
import { Configuration} from '../configuration'
import { Observable, of, from } from '../rxjsStub';
import {mergeMap, map} from  '../rxjsStub';
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

import { APIKeysApiRequestFactory, APIKeysApiResponseProcessor} from "../apis/APIKeysApi";
export class ObservableAPIKeysApi {
    private requestFactory: APIKeysApiRequestFactory;
    private responseProcessor: APIKeysApiResponseProcessor;
    private configuration: Configuration;

    public constructor(
        configuration: Configuration,
        requestFactory?: APIKeysApiRequestFactory,
        responseProcessor?: APIKeysApiResponseProcessor
    ) {
        this.configuration = configuration;
        this.requestFactory = requestFactory || new APIKeysApiRequestFactory(configuration);
        this.responseProcessor = responseProcessor || new APIKeysApiResponseProcessor();
    }

    /**
     * Updates the API key for the currently authenticated user.  Parameters ---------- user : dict     A dictionary containing user information retrieved     from the `get_user` dependency from `auth` module.     The dictionary is expected     to have the following structure:     ```     {         \'id\': <user_id>,         \'email\': <user_email>,         \'role\': <user_role>     }     ```  Returns ------- ResponseMessage     `detail` is the string of the new API key.
     * Update Usertoken
     */
    public updateUsertokenApiV1SecureUsersRenewPutWithHttpInfo(_options?: Configuration): Observable<HttpInfo<ResponseMessage>> {
        const requestContextPromise = this.requestFactory.updateUsertokenApiV1SecureUsersRenewPut(_options);

        // build promise chain
        let middlewarePreObservable = from<RequestContext>(requestContextPromise);
        for (let middleware of this.configuration.middleware) {
            middlewarePreObservable = middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => middleware.pre(ctx)));
        }

        return middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => this.configuration.httpApi.send(ctx))).
            pipe(mergeMap((response: ResponseContext) => {
                let middlewarePostObservable = of(response);
                for (let middleware of this.configuration.middleware) {
                    middlewarePostObservable = middlewarePostObservable.pipe(mergeMap((rsp: ResponseContext) => middleware.post(rsp)));
                }
                return middlewarePostObservable.pipe(map((rsp: ResponseContext) => this.responseProcessor.updateUsertokenApiV1SecureUsersRenewPutWithHttpInfo(rsp)));
            }));
    }

    /**
     * Updates the API key for the currently authenticated user.  Parameters ---------- user : dict     A dictionary containing user information retrieved     from the `get_user` dependency from `auth` module.     The dictionary is expected     to have the following structure:     ```     {         \'id\': <user_id>,         \'email\': <user_email>,         \'role\': <user_role>     }     ```  Returns ------- ResponseMessage     `detail` is the string of the new API key.
     * Update Usertoken
     */
    public updateUsertokenApiV1SecureUsersRenewPut(_options?: Configuration): Observable<ResponseMessage> {
        return this.updateUsertokenApiV1SecureUsersRenewPutWithHttpInfo(_options).pipe(map((apiResponse: HttpInfo<ResponseMessage>) => apiResponse.data));
    }

}

import { CommentsApiRequestFactory, CommentsApiResponseProcessor} from "../apis/CommentsApi";
export class ObservableCommentsApi {
    private requestFactory: CommentsApiRequestFactory;
    private responseProcessor: CommentsApiResponseProcessor;
    private configuration: Configuration;

    public constructor(
        configuration: Configuration,
        requestFactory?: CommentsApiRequestFactory,
        responseProcessor?: CommentsApiResponseProcessor
    ) {
        this.configuration = configuration;
        this.requestFactory = requestFactory || new CommentsApiRequestFactory(configuration);
        this.responseProcessor = responseProcessor || new CommentsApiResponseProcessor();
    }

    /**
     * Create a new comment.
     * Create Comment
     * @param commentModel 
     */
    public createCommentApiV1SecureCommentsPostWithHttpInfo(commentModel: CommentModel, _options?: Configuration): Observable<HttpInfo<any>> {
        const requestContextPromise = this.requestFactory.createCommentApiV1SecureCommentsPost(commentModel, _options);

        // build promise chain
        let middlewarePreObservable = from<RequestContext>(requestContextPromise);
        for (let middleware of this.configuration.middleware) {
            middlewarePreObservable = middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => middleware.pre(ctx)));
        }

        return middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => this.configuration.httpApi.send(ctx))).
            pipe(mergeMap((response: ResponseContext) => {
                let middlewarePostObservable = of(response);
                for (let middleware of this.configuration.middleware) {
                    middlewarePostObservable = middlewarePostObservable.pipe(mergeMap((rsp: ResponseContext) => middleware.post(rsp)));
                }
                return middlewarePostObservable.pipe(map((rsp: ResponseContext) => this.responseProcessor.createCommentApiV1SecureCommentsPostWithHttpInfo(rsp)));
            }));
    }

    /**
     * Create a new comment.
     * Create Comment
     * @param commentModel 
     */
    public createCommentApiV1SecureCommentsPost(commentModel: CommentModel, _options?: Configuration): Observable<any> {
        return this.createCommentApiV1SecureCommentsPostWithHttpInfo(commentModel, _options).pipe(map((apiResponse: HttpInfo<any>) => apiResponse.data));
    }

    /**
     * Delete Comment
     * @param cid 
     */
    public deleteCommentApiV1SecureCommentsCidDeleteWithHttpInfo(cid: number, _options?: Configuration): Observable<HttpInfo<any>> {
        const requestContextPromise = this.requestFactory.deleteCommentApiV1SecureCommentsCidDelete(cid, _options);

        // build promise chain
        let middlewarePreObservable = from<RequestContext>(requestContextPromise);
        for (let middleware of this.configuration.middleware) {
            middlewarePreObservable = middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => middleware.pre(ctx)));
        }

        return middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => this.configuration.httpApi.send(ctx))).
            pipe(mergeMap((response: ResponseContext) => {
                let middlewarePostObservable = of(response);
                for (let middleware of this.configuration.middleware) {
                    middlewarePostObservable = middlewarePostObservable.pipe(mergeMap((rsp: ResponseContext) => middleware.post(rsp)));
                }
                return middlewarePostObservable.pipe(map((rsp: ResponseContext) => this.responseProcessor.deleteCommentApiV1SecureCommentsCidDeleteWithHttpInfo(rsp)));
            }));
    }

    /**
     * Delete Comment
     * @param cid 
     */
    public deleteCommentApiV1SecureCommentsCidDelete(cid: number, _options?: Configuration): Observable<any> {
        return this.deleteCommentApiV1SecureCommentsCidDeleteWithHttpInfo(cid, _options).pipe(map((apiResponse: HttpInfo<any>) => apiResponse.data));
    }

    /**
     * Get Comments
     * @param cid 
     * @param random 
     * @param moderated 
     */
    public getCommentsApiV1SecureCommentsCidGetWithHttpInfo(cid: number, random?: boolean, moderated?: boolean, _options?: Configuration): Observable<HttpInfo<CommentResponse>> {
        const requestContextPromise = this.requestFactory.getCommentsApiV1SecureCommentsCidGet(cid, random, moderated, _options);

        // build promise chain
        let middlewarePreObservable = from<RequestContext>(requestContextPromise);
        for (let middleware of this.configuration.middleware) {
            middlewarePreObservable = middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => middleware.pre(ctx)));
        }

        return middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => this.configuration.httpApi.send(ctx))).
            pipe(mergeMap((response: ResponseContext) => {
                let middlewarePostObservable = of(response);
                for (let middleware of this.configuration.middleware) {
                    middlewarePostObservable = middlewarePostObservable.pipe(mergeMap((rsp: ResponseContext) => middleware.post(rsp)));
                }
                return middlewarePostObservable.pipe(map((rsp: ResponseContext) => this.responseProcessor.getCommentsApiV1SecureCommentsCidGetWithHttpInfo(rsp)));
            }));
    }

    /**
     * Get Comments
     * @param cid 
     * @param random 
     * @param moderated 
     */
    public getCommentsApiV1SecureCommentsCidGet(cid: number, random?: boolean, moderated?: boolean, _options?: Configuration): Observable<CommentResponse> {
        return this.getCommentsApiV1SecureCommentsCidGetWithHttpInfo(cid, random, moderated, _options).pipe(map((apiResponse: HttpInfo<CommentResponse>) => apiResponse.data));
    }

    /**
     * Get comments waiting for moderation from a conversation.  Returns ------- dict     A dictionary containing comments waiting for moderation.
     * Get Comments For Moderation
     * @param cid 
     */
    public getCommentsForModerationApiV1SecureCommentsCidModerateGetWithHttpInfo(cid: number, _options?: Configuration): Observable<HttpInfo<CommentResponse>> {
        const requestContextPromise = this.requestFactory.getCommentsForModerationApiV1SecureCommentsCidModerateGet(cid, _options);

        // build promise chain
        let middlewarePreObservable = from<RequestContext>(requestContextPromise);
        for (let middleware of this.configuration.middleware) {
            middlewarePreObservable = middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => middleware.pre(ctx)));
        }

        return middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => this.configuration.httpApi.send(ctx))).
            pipe(mergeMap((response: ResponseContext) => {
                let middlewarePostObservable = of(response);
                for (let middleware of this.configuration.middleware) {
                    middlewarePostObservable = middlewarePostObservable.pipe(mergeMap((rsp: ResponseContext) => middleware.post(rsp)));
                }
                return middlewarePostObservable.pipe(map((rsp: ResponseContext) => this.responseProcessor.getCommentsForModerationApiV1SecureCommentsCidModerateGetWithHttpInfo(rsp)));
            }));
    }

    /**
     * Get comments waiting for moderation from a conversation.  Returns ------- dict     A dictionary containing comments waiting for moderation.
     * Get Comments For Moderation
     * @param cid 
     */
    public getCommentsForModerationApiV1SecureCommentsCidModerateGet(cid: number, _options?: Configuration): Observable<CommentResponse> {
        return this.getCommentsForModerationApiV1SecureCommentsCidModerateGetWithHttpInfo(cid, _options).pipe(map((apiResponse: HttpInfo<CommentResponse>) => apiResponse.data));
    }

    /**
     * Update a comment.
     * Update Comment
     * @param commentModel 
     */
    public updateCommentApiV1SecureCommentsPutWithHttpInfo(commentModel: CommentModel, _options?: Configuration): Observable<HttpInfo<any>> {
        const requestContextPromise = this.requestFactory.updateCommentApiV1SecureCommentsPut(commentModel, _options);

        // build promise chain
        let middlewarePreObservable = from<RequestContext>(requestContextPromise);
        for (let middleware of this.configuration.middleware) {
            middlewarePreObservable = middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => middleware.pre(ctx)));
        }

        return middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => this.configuration.httpApi.send(ctx))).
            pipe(mergeMap((response: ResponseContext) => {
                let middlewarePostObservable = of(response);
                for (let middleware of this.configuration.middleware) {
                    middlewarePostObservable = middlewarePostObservable.pipe(mergeMap((rsp: ResponseContext) => middleware.post(rsp)));
                }
                return middlewarePostObservable.pipe(map((rsp: ResponseContext) => this.responseProcessor.updateCommentApiV1SecureCommentsPutWithHttpInfo(rsp)));
            }));
    }

    /**
     * Update a comment.
     * Update Comment
     * @param commentModel 
     */
    public updateCommentApiV1SecureCommentsPut(commentModel: CommentModel, _options?: Configuration): Observable<any> {
        return this.updateCommentApiV1SecureCommentsPutWithHttpInfo(commentModel, _options).pipe(map((apiResponse: HttpInfo<any>) => apiResponse.data));
    }

}

import { ConversationsApiRequestFactory, ConversationsApiResponseProcessor} from "../apis/ConversationsApi";
export class ObservableConversationsApi {
    private requestFactory: ConversationsApiRequestFactory;
    private responseProcessor: ConversationsApiResponseProcessor;
    private configuration: Configuration;

    public constructor(
        configuration: Configuration,
        requestFactory?: ConversationsApiRequestFactory,
        responseProcessor?: ConversationsApiResponseProcessor
    ) {
        this.configuration = configuration;
        this.requestFactory = requestFactory || new ConversationsApiRequestFactory(configuration);
        this.responseProcessor = responseProcessor || new ConversationsApiResponseProcessor();
    }

    /**
     * Create a new conversation.  Parameters ---------- create_conversation : ConversationModel     Conversation information to create. user : dict     Authenticated user information.
     * Create Conversation
     * @param conversationModel 
     */
    public createConversationApiV1SecureConversationsPostWithHttpInfo(conversationModel: ConversationModel, _options?: Configuration): Observable<HttpInfo<any>> {
        const requestContextPromise = this.requestFactory.createConversationApiV1SecureConversationsPost(conversationModel, _options);

        // build promise chain
        let middlewarePreObservable = from<RequestContext>(requestContextPromise);
        for (let middleware of this.configuration.middleware) {
            middlewarePreObservable = middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => middleware.pre(ctx)));
        }

        return middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => this.configuration.httpApi.send(ctx))).
            pipe(mergeMap((response: ResponseContext) => {
                let middlewarePostObservable = of(response);
                for (let middleware of this.configuration.middleware) {
                    middlewarePostObservable = middlewarePostObservable.pipe(mergeMap((rsp: ResponseContext) => middleware.post(rsp)));
                }
                return middlewarePostObservable.pipe(map((rsp: ResponseContext) => this.responseProcessor.createConversationApiV1SecureConversationsPostWithHttpInfo(rsp)));
            }));
    }

    /**
     * Create a new conversation.  Parameters ---------- create_conversation : ConversationModel     Conversation information to create. user : dict     Authenticated user information.
     * Create Conversation
     * @param conversationModel 
     */
    public createConversationApiV1SecureConversationsPost(conversationModel: ConversationModel, _options?: Configuration): Observable<any> {
        return this.createConversationApiV1SecureConversationsPostWithHttpInfo(conversationModel, _options).pipe(map((apiResponse: HttpInfo<any>) => apiResponse.data));
    }

    /**
     * Delete Conversation
     * @param cid 
     */
    public deleteConversationApiV1SecureConversationsCidDeleteWithHttpInfo(cid: number, _options?: Configuration): Observable<HttpInfo<any>> {
        const requestContextPromise = this.requestFactory.deleteConversationApiV1SecureConversationsCidDelete(cid, _options);

        // build promise chain
        let middlewarePreObservable = from<RequestContext>(requestContextPromise);
        for (let middleware of this.configuration.middleware) {
            middlewarePreObservable = middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => middleware.pre(ctx)));
        }

        return middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => this.configuration.httpApi.send(ctx))).
            pipe(mergeMap((response: ResponseContext) => {
                let middlewarePostObservable = of(response);
                for (let middleware of this.configuration.middleware) {
                    middlewarePostObservable = middlewarePostObservable.pipe(mergeMap((rsp: ResponseContext) => middleware.post(rsp)));
                }
                return middlewarePostObservable.pipe(map((rsp: ResponseContext) => this.responseProcessor.deleteConversationApiV1SecureConversationsCidDeleteWithHttpInfo(rsp)));
            }));
    }

    /**
     * Delete Conversation
     * @param cid 
     */
    public deleteConversationApiV1SecureConversationsCidDelete(cid: number, _options?: Configuration): Observable<any> {
        return this.deleteConversationApiV1SecureConversationsCidDeleteWithHttpInfo(cid, _options).pipe(map((apiResponse: HttpInfo<any>) => apiResponse.data));
    }

    /**
     * Get all conversations for the authenticated user.  Returns ------- dict     A dictionary containing all conversations for the user.
     * Get All Conversations
     */
    public getAllConversationsApiV1SecureConversationsAllGetWithHttpInfo(_options?: Configuration): Observable<HttpInfo<ConversationResponse>> {
        const requestContextPromise = this.requestFactory.getAllConversationsApiV1SecureConversationsAllGet(_options);

        // build promise chain
        let middlewarePreObservable = from<RequestContext>(requestContextPromise);
        for (let middleware of this.configuration.middleware) {
            middlewarePreObservable = middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => middleware.pre(ctx)));
        }

        return middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => this.configuration.httpApi.send(ctx))).
            pipe(mergeMap((response: ResponseContext) => {
                let middlewarePostObservable = of(response);
                for (let middleware of this.configuration.middleware) {
                    middlewarePostObservable = middlewarePostObservable.pipe(mergeMap((rsp: ResponseContext) => middleware.post(rsp)));
                }
                return middlewarePostObservable.pipe(map((rsp: ResponseContext) => this.responseProcessor.getAllConversationsApiV1SecureConversationsAllGetWithHttpInfo(rsp)));
            }));
    }

    /**
     * Get all conversations for the authenticated user.  Returns ------- dict     A dictionary containing all conversations for the user.
     * Get All Conversations
     */
    public getAllConversationsApiV1SecureConversationsAllGet(_options?: Configuration): Observable<ConversationResponse> {
        return this.getAllConversationsApiV1SecureConversationsAllGetWithHttpInfo(_options).pipe(map((apiResponse: HttpInfo<ConversationResponse>) => apiResponse.data));
    }

    /**
     * Get a conversation by ID.  Returns ------- dict     A dictionary containing the conversation details.
     * Get Conversation
     * @param cid 
     */
    public getConversationApiV1SecureConversationsCidGetWithHttpInfo(cid: number, _options?: Configuration): Observable<HttpInfo<ResponseMessage>> {
        const requestContextPromise = this.requestFactory.getConversationApiV1SecureConversationsCidGet(cid, _options);

        // build promise chain
        let middlewarePreObservable = from<RequestContext>(requestContextPromise);
        for (let middleware of this.configuration.middleware) {
            middlewarePreObservable = middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => middleware.pre(ctx)));
        }

        return middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => this.configuration.httpApi.send(ctx))).
            pipe(mergeMap((response: ResponseContext) => {
                let middlewarePostObservable = of(response);
                for (let middleware of this.configuration.middleware) {
                    middlewarePostObservable = middlewarePostObservable.pipe(mergeMap((rsp: ResponseContext) => middleware.post(rsp)));
                }
                return middlewarePostObservable.pipe(map((rsp: ResponseContext) => this.responseProcessor.getConversationApiV1SecureConversationsCidGetWithHttpInfo(rsp)));
            }));
    }

    /**
     * Get a conversation by ID.  Returns ------- dict     A dictionary containing the conversation details.
     * Get Conversation
     * @param cid 
     */
    public getConversationApiV1SecureConversationsCidGet(cid: number, _options?: Configuration): Observable<ResponseMessage> {
        return this.getConversationApiV1SecureConversationsCidGetWithHttpInfo(cid, _options).pipe(map((apiResponse: HttpInfo<ResponseMessage>) => apiResponse.data));
    }

    /**
     * Update a conversation.  Parameters ---------- update_conversation : ConversationModel     Conversation update information. user : dict     Authenticated user information.
     * Update Conversation
     * @param conversationModel 
     */
    public updateConversationApiV1SecureConversationsPutWithHttpInfo(conversationModel: ConversationModel, _options?: Configuration): Observable<HttpInfo<any>> {
        const requestContextPromise = this.requestFactory.updateConversationApiV1SecureConversationsPut(conversationModel, _options);

        // build promise chain
        let middlewarePreObservable = from<RequestContext>(requestContextPromise);
        for (let middleware of this.configuration.middleware) {
            middlewarePreObservable = middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => middleware.pre(ctx)));
        }

        return middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => this.configuration.httpApi.send(ctx))).
            pipe(mergeMap((response: ResponseContext) => {
                let middlewarePostObservable = of(response);
                for (let middleware of this.configuration.middleware) {
                    middlewarePostObservable = middlewarePostObservable.pipe(mergeMap((rsp: ResponseContext) => middleware.post(rsp)));
                }
                return middlewarePostObservable.pipe(map((rsp: ResponseContext) => this.responseProcessor.updateConversationApiV1SecureConversationsPutWithHttpInfo(rsp)));
            }));
    }

    /**
     * Update a conversation.  Parameters ---------- update_conversation : ConversationModel     Conversation update information. user : dict     Authenticated user information.
     * Update Conversation
     * @param conversationModel 
     */
    public updateConversationApiV1SecureConversationsPut(conversationModel: ConversationModel, _options?: Configuration): Observable<any> {
        return this.updateConversationApiV1SecureConversationsPutWithHttpInfo(conversationModel, _options).pipe(map((apiResponse: HttpInfo<any>) => apiResponse.data));
    }

}

import { DefaultApiRequestFactory, DefaultApiResponseProcessor} from "../apis/DefaultApi";
export class ObservableDefaultApi {
    private requestFactory: DefaultApiRequestFactory;
    private responseProcessor: DefaultApiResponseProcessor;
    private configuration: Configuration;

    public constructor(
        configuration: Configuration,
        requestFactory?: DefaultApiRequestFactory,
        responseProcessor?: DefaultApiResponseProcessor
    ) {
        this.configuration = configuration;
        this.requestFactory = requestFactory || new DefaultApiRequestFactory(configuration);
        this.responseProcessor = responseProcessor || new DefaultApiResponseProcessor();
    }

    /**
     * This endpoint is used to check if the database connection is healthy.  Returns ------- dict     A dictionary containing the status of the database connection.     - If the connection is healthy, the dictionary will contain     {\"detail\": \"OK\"}.     - If the connection is not healthy, the dictionary will contain     {\"detail\": \"DB conn failed\"}.
     * Get Testroute
     */
    public getTestrouteApiV1PublicGetWithHttpInfo(_options?: Configuration): Observable<HttpInfo<any>> {
        const requestContextPromise = this.requestFactory.getTestrouteApiV1PublicGet(_options);

        // build promise chain
        let middlewarePreObservable = from<RequestContext>(requestContextPromise);
        for (let middleware of this.configuration.middleware) {
            middlewarePreObservable = middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => middleware.pre(ctx)));
        }

        return middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => this.configuration.httpApi.send(ctx))).
            pipe(mergeMap((response: ResponseContext) => {
                let middlewarePostObservable = of(response);
                for (let middleware of this.configuration.middleware) {
                    middlewarePostObservable = middlewarePostObservable.pipe(mergeMap((rsp: ResponseContext) => middleware.post(rsp)));
                }
                return middlewarePostObservable.pipe(map((rsp: ResponseContext) => this.responseProcessor.getTestrouteApiV1PublicGetWithHttpInfo(rsp)));
            }));
    }

    /**
     * This endpoint is used to check if the database connection is healthy.  Returns ------- dict     A dictionary containing the status of the database connection.     - If the connection is healthy, the dictionary will contain     {\"detail\": \"OK\"}.     - If the connection is not healthy, the dictionary will contain     {\"detail\": \"DB conn failed\"}.
     * Get Testroute
     */
    public getTestrouteApiV1PublicGet(_options?: Configuration): Observable<any> {
        return this.getTestrouteApiV1PublicGetWithHttpInfo(_options).pipe(map((apiResponse: HttpInfo<any>) => apiResponse.data));
    }

}

import { UserApiRequestFactory, UserApiResponseProcessor} from "../apis/UserApi";
export class ObservableUserApi {
    private requestFactory: UserApiRequestFactory;
    private responseProcessor: UserApiResponseProcessor;
    private configuration: Configuration;

    public constructor(
        configuration: Configuration,
        requestFactory?: UserApiRequestFactory,
        responseProcessor?: UserApiResponseProcessor
    ) {
        this.configuration = configuration;
        this.requestFactory = requestFactory || new UserApiRequestFactory(configuration);
        this.responseProcessor = responseProcessor || new UserApiResponseProcessor();
    }

    /**
     * Create a new user profile.  Parameters ---------- user_profile : UserProfile     User profile information. user : dict     Authenticated user information.
     * Create Userprofile
     * @param userProfile 
     */
    public createUserprofileApiV1SecureUsersProfilePostWithHttpInfo(userProfile: UserProfile, _options?: Configuration): Observable<HttpInfo<ResponseMessage>> {
        const requestContextPromise = this.requestFactory.createUserprofileApiV1SecureUsersProfilePost(userProfile, _options);

        // build promise chain
        let middlewarePreObservable = from<RequestContext>(requestContextPromise);
        for (let middleware of this.configuration.middleware) {
            middlewarePreObservable = middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => middleware.pre(ctx)));
        }

        return middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => this.configuration.httpApi.send(ctx))).
            pipe(mergeMap((response: ResponseContext) => {
                let middlewarePostObservable = of(response);
                for (let middleware of this.configuration.middleware) {
                    middlewarePostObservable = middlewarePostObservable.pipe(mergeMap((rsp: ResponseContext) => middleware.post(rsp)));
                }
                return middlewarePostObservable.pipe(map((rsp: ResponseContext) => this.responseProcessor.createUserprofileApiV1SecureUsersProfilePostWithHttpInfo(rsp)));
            }));
    }

    /**
     * Create a new user profile.  Parameters ---------- user_profile : UserProfile     User profile information. user : dict     Authenticated user information.
     * Create Userprofile
     * @param userProfile 
     */
    public createUserprofileApiV1SecureUsersProfilePost(userProfile: UserProfile, _options?: Configuration): Observable<ResponseMessage> {
        return this.createUserprofileApiV1SecureUsersProfilePostWithHttpInfo(userProfile, _options).pipe(map((apiResponse: HttpInfo<ResponseMessage>) => apiResponse.data));
    }

    /**
     * Delete Userprofile
     */
    public deleteUserprofileApiV1SecureUsersProfileDeleteWithHttpInfo(_options?: Configuration): Observable<HttpInfo<any>> {
        const requestContextPromise = this.requestFactory.deleteUserprofileApiV1SecureUsersProfileDelete(_options);

        // build promise chain
        let middlewarePreObservable = from<RequestContext>(requestContextPromise);
        for (let middleware of this.configuration.middleware) {
            middlewarePreObservable = middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => middleware.pre(ctx)));
        }

        return middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => this.configuration.httpApi.send(ctx))).
            pipe(mergeMap((response: ResponseContext) => {
                let middlewarePostObservable = of(response);
                for (let middleware of this.configuration.middleware) {
                    middlewarePostObservable = middlewarePostObservable.pipe(mergeMap((rsp: ResponseContext) => middleware.post(rsp)));
                }
                return middlewarePostObservable.pipe(map((rsp: ResponseContext) => this.responseProcessor.deleteUserprofileApiV1SecureUsersProfileDeleteWithHttpInfo(rsp)));
            }));
    }

    /**
     * Delete Userprofile
     */
    public deleteUserprofileApiV1SecureUsersProfileDelete(_options?: Configuration): Observable<any> {
        return this.deleteUserprofileApiV1SecureUsersProfileDeleteWithHttpInfo(_options).pipe(map((apiResponse: HttpInfo<any>) => apiResponse.data));
    }

    /**
     * This endpoint returns information about the currently authenticated user.  Parameters ---------- user : dict     A dictionary containing user information retrieved     from the `get_user` dependency from `auth` module.     The dictionary is expected to have the following structure:     ```     {         \'id\': <user_id>,         \'email\': <user_email>,         \'role\': <user_role>     }     ```  Returns ------- ResponseMessage     `detail` is `UserResponseMessage` containing the user\'s id, email, and role.
     * Get Testroute
     */
    public getTestrouteApiV1SecureGetWithHttpInfo(_options?: Configuration): Observable<HttpInfo<ResponseMessage>> {
        const requestContextPromise = this.requestFactory.getTestrouteApiV1SecureGet(_options);

        // build promise chain
        let middlewarePreObservable = from<RequestContext>(requestContextPromise);
        for (let middleware of this.configuration.middleware) {
            middlewarePreObservable = middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => middleware.pre(ctx)));
        }

        return middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => this.configuration.httpApi.send(ctx))).
            pipe(mergeMap((response: ResponseContext) => {
                let middlewarePostObservable = of(response);
                for (let middleware of this.configuration.middleware) {
                    middlewarePostObservable = middlewarePostObservable.pipe(mergeMap((rsp: ResponseContext) => middleware.post(rsp)));
                }
                return middlewarePostObservable.pipe(map((rsp: ResponseContext) => this.responseProcessor.getTestrouteApiV1SecureGetWithHttpInfo(rsp)));
            }));
    }

    /**
     * This endpoint returns information about the currently authenticated user.  Parameters ---------- user : dict     A dictionary containing user information retrieved     from the `get_user` dependency from `auth` module.     The dictionary is expected to have the following structure:     ```     {         \'id\': <user_id>,         \'email\': <user_email>,         \'role\': <user_role>     }     ```  Returns ------- ResponseMessage     `detail` is `UserResponseMessage` containing the user\'s id, email, and role.
     * Get Testroute
     */
    public getTestrouteApiV1SecureGet(_options?: Configuration): Observable<ResponseMessage> {
        return this.getTestrouteApiV1SecureGetWithHttpInfo(_options).pipe(map((apiResponse: HttpInfo<ResponseMessage>) => apiResponse.data));
    }

    /**
     * Get Userauth
     * @param userProfile 
     */
    public getUserauthApiV1SecureUsersAuthPostWithHttpInfo(userProfile: UserProfile, _options?: Configuration): Observable<HttpInfo<ResponseMessage>> {
        const requestContextPromise = this.requestFactory.getUserauthApiV1SecureUsersAuthPost(userProfile, _options);

        // build promise chain
        let middlewarePreObservable = from<RequestContext>(requestContextPromise);
        for (let middleware of this.configuration.middleware) {
            middlewarePreObservable = middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => middleware.pre(ctx)));
        }

        return middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => this.configuration.httpApi.send(ctx))).
            pipe(mergeMap((response: ResponseContext) => {
                let middlewarePostObservable = of(response);
                for (let middleware of this.configuration.middleware) {
                    middlewarePostObservable = middlewarePostObservable.pipe(mergeMap((rsp: ResponseContext) => middleware.post(rsp)));
                }
                return middlewarePostObservable.pipe(map((rsp: ResponseContext) => this.responseProcessor.getUserauthApiV1SecureUsersAuthPostWithHttpInfo(rsp)));
            }));
    }

    /**
     * Get Userauth
     * @param userProfile 
     */
    public getUserauthApiV1SecureUsersAuthPost(userProfile: UserProfile, _options?: Configuration): Observable<ResponseMessage> {
        return this.getUserauthApiV1SecureUsersAuthPostWithHttpInfo(userProfile, _options).pipe(map((apiResponse: HttpInfo<ResponseMessage>) => apiResponse.data));
    }

    /**
     * This endpoint returns information about the currently authenticated user.  Parameters ---------- user : dict     A dictionary containing user information retrieved     from the `get_user` dependency from `auth` module.     The dictionary is expected     to have the following structure:     ```     {         \'id\': <user_id>,         \'email\': <user_email>,         \'role\': <user_role>     }     ```  Returns ------- ResponseMessage     `detail` is `UserResponseMessage` containing the user\'s id, email, and role.
     * Get Userprofile
     */
    public getUserprofileApiV1SecureUsersProfileGetWithHttpInfo(_options?: Configuration): Observable<HttpInfo<ResponseMessage>> {
        const requestContextPromise = this.requestFactory.getUserprofileApiV1SecureUsersProfileGet(_options);

        // build promise chain
        let middlewarePreObservable = from<RequestContext>(requestContextPromise);
        for (let middleware of this.configuration.middleware) {
            middlewarePreObservable = middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => middleware.pre(ctx)));
        }

        return middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => this.configuration.httpApi.send(ctx))).
            pipe(mergeMap((response: ResponseContext) => {
                let middlewarePostObservable = of(response);
                for (let middleware of this.configuration.middleware) {
                    middlewarePostObservable = middlewarePostObservable.pipe(mergeMap((rsp: ResponseContext) => middleware.post(rsp)));
                }
                return middlewarePostObservable.pipe(map((rsp: ResponseContext) => this.responseProcessor.getUserprofileApiV1SecureUsersProfileGetWithHttpInfo(rsp)));
            }));
    }

    /**
     * This endpoint returns information about the currently authenticated user.  Parameters ---------- user : dict     A dictionary containing user information retrieved     from the `get_user` dependency from `auth` module.     The dictionary is expected     to have the following structure:     ```     {         \'id\': <user_id>,         \'email\': <user_email>,         \'role\': <user_role>     }     ```  Returns ------- ResponseMessage     `detail` is `UserResponseMessage` containing the user\'s id, email, and role.
     * Get Userprofile
     */
    public getUserprofileApiV1SecureUsersProfileGet(_options?: Configuration): Observable<ResponseMessage> {
        return this.getUserprofileApiV1SecureUsersProfileGetWithHttpInfo(_options).pipe(map((apiResponse: HttpInfo<ResponseMessage>) => apiResponse.data));
    }

    /**
     * This endpoint returns the role of the currently authenticated user.  Parameters ---------- user : dict     A dictionary containing user information retrieved     from the `get_user` dependency from `auth` module.     The dictionary is expected to have the following structure:     ```     {         \'id\': <user_id>,         \'email\': <user_email>,         \'role\': <user_role>     }  Returns ------- ResponseMessage     `detail` string of the user\'s role.
     * Get Userrole
     */
    public getUserroleApiV1SecureUsersRoleGetWithHttpInfo(_options?: Configuration): Observable<HttpInfo<ResponseMessage>> {
        const requestContextPromise = this.requestFactory.getUserroleApiV1SecureUsersRoleGet(_options);

        // build promise chain
        let middlewarePreObservable = from<RequestContext>(requestContextPromise);
        for (let middleware of this.configuration.middleware) {
            middlewarePreObservable = middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => middleware.pre(ctx)));
        }

        return middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => this.configuration.httpApi.send(ctx))).
            pipe(mergeMap((response: ResponseContext) => {
                let middlewarePostObservable = of(response);
                for (let middleware of this.configuration.middleware) {
                    middlewarePostObservable = middlewarePostObservable.pipe(mergeMap((rsp: ResponseContext) => middleware.post(rsp)));
                }
                return middlewarePostObservable.pipe(map((rsp: ResponseContext) => this.responseProcessor.getUserroleApiV1SecureUsersRoleGetWithHttpInfo(rsp)));
            }));
    }

    /**
     * This endpoint returns the role of the currently authenticated user.  Parameters ---------- user : dict     A dictionary containing user information retrieved     from the `get_user` dependency from `auth` module.     The dictionary is expected to have the following structure:     ```     {         \'id\': <user_id>,         \'email\': <user_email>,         \'role\': <user_role>     }  Returns ------- ResponseMessage     `detail` string of the user\'s role.
     * Get Userrole
     */
    public getUserroleApiV1SecureUsersRoleGet(_options?: Configuration): Observable<ResponseMessage> {
        return this.getUserroleApiV1SecureUsersRoleGetWithHttpInfo(_options).pipe(map((apiResponse: HttpInfo<ResponseMessage>) => apiResponse.data));
    }

    /**
     * Update the authenticated user\'s profile.  Parameters ---------- update_user : UpdateUserProfile     User profile information to update. user : dict     Authenticated user information.
     * Update Userprofile
     * @param userProfile 
     */
    public updateUserprofileApiV1SecureUsersProfilePutWithHttpInfo(userProfile: UserProfile, _options?: Configuration): Observable<HttpInfo<any>> {
        const requestContextPromise = this.requestFactory.updateUserprofileApiV1SecureUsersProfilePut(userProfile, _options);

        // build promise chain
        let middlewarePreObservable = from<RequestContext>(requestContextPromise);
        for (let middleware of this.configuration.middleware) {
            middlewarePreObservable = middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => middleware.pre(ctx)));
        }

        return middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => this.configuration.httpApi.send(ctx))).
            pipe(mergeMap((response: ResponseContext) => {
                let middlewarePostObservable = of(response);
                for (let middleware of this.configuration.middleware) {
                    middlewarePostObservable = middlewarePostObservable.pipe(mergeMap((rsp: ResponseContext) => middleware.post(rsp)));
                }
                return middlewarePostObservable.pipe(map((rsp: ResponseContext) => this.responseProcessor.updateUserprofileApiV1SecureUsersProfilePutWithHttpInfo(rsp)));
            }));
    }

    /**
     * Update the authenticated user\'s profile.  Parameters ---------- update_user : UpdateUserProfile     User profile information to update. user : dict     Authenticated user information.
     * Update Userprofile
     * @param userProfile 
     */
    public updateUserprofileApiV1SecureUsersProfilePut(userProfile: UserProfile, _options?: Configuration): Observable<any> {
        return this.updateUserprofileApiV1SecureUsersProfilePutWithHttpInfo(userProfile, _options).pipe(map((apiResponse: HttpInfo<any>) => apiResponse.data));
    }

    /**
     * Updates the API key for the currently authenticated user.  Parameters ---------- user : dict     A dictionary containing user information retrieved     from the `get_user` dependency from `auth` module.     The dictionary is expected     to have the following structure:     ```     {         \'id\': <user_id>,         \'email\': <user_email>,         \'role\': <user_role>     }     ```  Returns ------- ResponseMessage     `detail` is the string of the new API key.
     * Update Usertoken
     */
    public updateUsertokenApiV1SecureUsersRenewPutWithHttpInfo(_options?: Configuration): Observable<HttpInfo<ResponseMessage>> {
        const requestContextPromise = this.requestFactory.updateUsertokenApiV1SecureUsersRenewPut(_options);

        // build promise chain
        let middlewarePreObservable = from<RequestContext>(requestContextPromise);
        for (let middleware of this.configuration.middleware) {
            middlewarePreObservable = middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => middleware.pre(ctx)));
        }

        return middlewarePreObservable.pipe(mergeMap((ctx: RequestContext) => this.configuration.httpApi.send(ctx))).
            pipe(mergeMap((response: ResponseContext) => {
                let middlewarePostObservable = of(response);
                for (let middleware of this.configuration.middleware) {
                    middlewarePostObservable = middlewarePostObservable.pipe(mergeMap((rsp: ResponseContext) => middleware.post(rsp)));
                }
                return middlewarePostObservable.pipe(map((rsp: ResponseContext) => this.responseProcessor.updateUsertokenApiV1SecureUsersRenewPutWithHttpInfo(rsp)));
            }));
    }

    /**
     * Updates the API key for the currently authenticated user.  Parameters ---------- user : dict     A dictionary containing user information retrieved     from the `get_user` dependency from `auth` module.     The dictionary is expected     to have the following structure:     ```     {         \'id\': <user_id>,         \'email\': <user_email>,         \'role\': <user_role>     }     ```  Returns ------- ResponseMessage     `detail` is the string of the new API key.
     * Update Usertoken
     */
    public updateUsertokenApiV1SecureUsersRenewPut(_options?: Configuration): Observable<ResponseMessage> {
        return this.updateUsertokenApiV1SecureUsersRenewPutWithHttpInfo(_options).pipe(map((apiResponse: HttpInfo<ResponseMessage>) => apiResponse.data));
    }

}
