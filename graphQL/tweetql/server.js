import { ApolloServer, gql } from "apollo-server";

// Graphql Schema Definition Language
const typeDefs = gql`
  type User {
    id: ID!
    username: String!
    firstname: String
    lastname: String
  }

  type Tweet {
    id: ID!
    text: String!
    author: User!
  }

  type Query {
    allTweets: [Tweet!]!
    tweet(id: ID!): Tweet
  }

  type Mutation {
    postTweet(text: String!, userID: ID!): Tweet!
    deleteTweet(id: ID!): Boolean!
  }
`;

const server = new ApolloServer({ typeDefs });
server.listen().then(({ url }) => {
  console.log(`🚀 Server ready at ${url}`);
});
