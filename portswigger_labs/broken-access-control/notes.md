# Broken Access Control

The concepts of **Authentication**, **Session Management**, and **Access Control** are all critical components in ensuring the security of systems, especially in web and network environments. However, they serve different purposes and operate at distinct stages of a user's interaction with a system.

### 1. **Authentication**
Authentication is the process of verifying the identity of a user or entity trying to access a system. It ensures that the person or entity requesting access is who they claim to be. 

- **Example**: When you log in to a website using your username and password, the website authenticates your identity to confirm that you are authorized to access your account.
  
  **Methods**:  
  - Password-based authentication  
  - Multi-factor authentication (MFA)  
  - Biometric authentication (fingerprint, facial recognition)  
  - Token-based authentication (e.g., OAuth, JWT)

### 2. **Session Management**
Session management refers to the handling of user sessions after authentication, ensuring that a user remains authenticated and that their activities within a session are tracked securely.

- **Example**: After successfully logging in, a website or app creates a session for the user. The session may store a session ID or token in cookies or local storage to allow the user to remain logged in as they interact with the site, without requiring re-authentication on each page request.
  
  **Key Concepts**:  
  - **Session IDs**: A unique identifier assigned to the user after login to track the session.  
  - **Session Timeout**: After a certain period of inactivity, a session may expire, requiring re-authentication.  
  - **Session Cookies**: Cookies that store session information in the user's browser.  
  - **Token Expiry**: In cases like JWT, tokens may have expiration times to limit the session duration.

### 3. **Access Control**
Access control is the process of defining and enforcing who can access what resources and what actions they can perform within the system. It's about regulating permissions based on roles, attributes, or policies.

- **Example**: In a company’s internal system, only managers may have access to financial records, while regular employees may only view their own work data. This control ensures that users can only access the information and features they are authorized to use.
  
  **Types**:
  - **Role-based access control (RBAC)**: Users are assigned roles, and each role has specific permissions.
  - **Attribute-based access control (ABAC)**: Access is based on attributes (e.g., user’s department, clearance level).
  - **Discretionary access control (DAC)**: Resource owners determine who has access to resources.

### Summary of Differences:
- **Authentication** ensures that the user is who they say they are.
- **Session Management** manages the user’s active state, maintaining the session after authentication.
- **Access Control** governs what resources the authenticated and active user can access and what actions they can perform.

These three work together to secure systems by ensuring only authenticated users can access the system, tracking their activities during a session, and enforcing the correct level of access throughout their interaction with the system.
