ThisBuild / scalaVersion := "2.12.12"
ThisBuild / organization := "com.gropyus"
ThisBuild / scapegoatVersion := "1.3.11"

assemblyMergeStrategy in assembly := {
  case "module-info.class" => MergeStrategy.discard
  case x =>
    val oldStrategy = (assemblyMergeStrategy in assembly).value
    oldStrategy(x)
}

lazy val app = (project in file("."))
  .configs(IntegrationTest)
  .settings(
    name := "jobs",
    version := "0.1.0-SNAPSHOT",
    Defaults.itSettings,
    parallelExecution in IntegrationTest := false,
    mainClass in assembly := Some("com.gropyus.Main"),
    test in assembly := {},
    libraryDependencies += "com.typesafe"               % "config"               % "1.4.1",
    libraryDependencies += "com.typesafe.akka"          %% "akka-actor-typed"    % akkaVersion,
    libraryDependencies += "com.typesafe.akka"          %% "akka-stream"         % akkaVersion,
    libraryDependencies += "com.typesafe.akka"          %% "akka-http"           % akkaHttpVersion,
    libraryDependencies += "ch.megard"                  %% "akka-http-cors"      % "1.1.1",
    libraryDependencies += "ch.qos.logback"             % "logback-classic"      % "1.2.3",
    libraryDependencies += "com.typesafe.scala-logging" %% "scala-logging"       % "3.9.2",
    libraryDependencies += "org.scalatest"              %% "scalatest"           % "3.2.5" % "it,test",
    libraryDependencies += "org.mockito"                %% "mockito-scala"       % "1.16.29" % Test,
    libraryDependencies += "com.typesafe.akka"          %% "akka-stream-testkit" % akkaVersion % "it,test",
    libraryDependencies += "com.typesafe.akka"          %% "akka-http-testkit"   % akkaHttpVersion % "it,test"
  )
