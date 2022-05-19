import { ApolloServer, gql } from "apollo-server";
import fetch from "node-fetch";

let tweets = [
  { id: "1", text: "First one", userID: "1" },
  { id: "2", text: "Second one", userID: "2" },
];

let users = [
  { id: "1", firstname: "Yoon", lastname: "roki" },
  { id: "2", firstname: "Jonji", lastname: "hi" },
  { id: "3", firstname: "Kim", lastname: "toki" },
];

// Graphql Schema Definition Language
const typeDefs = gql`
  type User {
    id: ID!
    """
    The username is the sum firstname + lastname as a string
    """
    username: String!
    firstname: String!
    lastname: String!
  }

  """
  Tweet object resprsents a resource of a Tweet.
  """
  type Tweet {
    id: ID!
    text: String!
    author: User!
  }

  type Query {
    allMovies: [Movie!]!
    allUsers: [User!]!
    allTweets: [Tweet!]!
    tweet(id: ID!): Tweet
    movie(id: String!): Movie
  }

  type Mutation {
    postTweet(text: String!, userID: ID!): Tweet!
    """
    Delete a Tweet if found, else returns false
    """
    deleteTweet(id: ID!): Boolean!
  }

  type Movie {
    id: Int!
    url: String!
    imdb_code: String!
    title: String
    title_english: String!
    title_long: String!
    slug: String!
    year: Int!
    rating: Float!
    runtime: Float!
    genres: [String!]!
    summary: String
    description_full: String!
    synopsis: String
    yt_trailer_code: String!
    language: String!
    mpa_rating: String!
    background_image: String!
    background_image_original: String!
    small_cover_image: String!
    medium_cover_image: String!
    large_cover_image: String!
    state: String
    date_uploaded: String!
    date_uploaded_unix: Int!
  }
`;

const resolvers = {
  // Query Resolvers
  Query: {
    allUsers() {
      return users;
    },

    allTweets() {
      return tweets;
    },

    tweet(_, { id }) {
      return tweets.find((tweet) => tweet.id === id);
    },

    // Migrating from REST to GraphQL
    allMovies() {
      return fetch("https://yts.mx/api/v2/list_movies.json")
        .then((resp) => resp.json())
        .then((json) => json.data.movies);
    },

    movie(_, { id }) {
      return fetch(`https://yts.mx/api/v2/movie_details.json?movie_id=${id}`)
        .then((resp) => resp.json())
        .then((json) => json.data.movie);
    },
  },

  //  Mutation Resolvers
  Mutation: {
    postTweet(_, { text, userID }) {
      const newTweet = {
        id: tweets.length + 1,
        text: text,
        userID: userID,
      };

      const user = users.find((user) => user.id === userID);
      if (user) {
        tweets.push(newTweet);
        return newTweet;
      } else {
        throw new Error("The user does not exist.");
      }
    },

    deleteTweet(_, { id }) {
      const tweet = tweets.find((tweet) => tweet.id === id);
      if (!tweet) return false;
      tweets = tweets.filter((tweet) => tweet.id !== id);
      return true;
    },
  },

  // Type Resolvers
  User: {
    username({ firstname, lastname }) {
      return `${firstname} ${lastname}`;
    },
  },

  Tweet: {
    author({ userID }) {
      return users.find((user) => user.id === userID);
    },
  },
};

const server = new ApolloServer({ typeDefs, resolvers });
server.listen().then(({ url }) => {
  console.log(`🚀 Server ready at ${url}`);
});
