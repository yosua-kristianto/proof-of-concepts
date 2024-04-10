(*
NOT ADDED TO COMPILED
*)

module GPT_san

open System
open System.Net.Sockets
open System.Text
open Newtonsoft.Json
open System.Threading.Tasks

type SomeData = {
    test: string
    lala: int
}

let SocketCall (i: int) = 
    async {
        let SOCKET_PORT: int = 55717

        let startTime = DateTime.Now

        let client = new TcpClient()
        do! client.ConnectAsync("localhost", SOCKET_PORT) |> Async.AwaitTask
    
        try
            let request: SomeData = { test = "Nyenye-" + i.ToString();  lala = i }

            use stream = client.GetStream()
    
            // Send Request to server
            let requestBytes = Encoding.ASCII.GetBytes(JsonConvert.SerializeObject(request))
            do! stream.WriteAsync(requestBytes, 0, requestBytes.Length) |> Async.AwaitTask

            // Receive response from server
            let responseBytes = Array.zeroCreate<byte> 1024
            let! bytesRead = stream.ReadAsync(responseBytes, 0, responseBytes.Length) |> Async.AwaitTask
            let response: string = Encoding.ASCII.GetString(responseBytes, 0, bytesRead)

            let timer: float = (DateTime.Now - startTime).TotalSeconds
            printfn "%A processed in %f second(s)" response timer
        finally
            client.Dispose()
    }


[<EntryPoint>]
let Main (args: string array) =
    
    let mutable taskTemp: int array = [||]

    for i in 0 .. 750000 do
        taskTemp <- Array.append taskTemp [| i |]

        if taskTemp.Length % 30 = 0 && taskTemp.Length <> 0 then
            let tasks = [ for f in taskTemp -> SocketCall f ]
            tasks 
            |> Async.Parallel
            |> Async.RunSynchronously |> ignore

            // Do something that cannot be run synchronously
            for f in 0 .. taskTemp.Length - 1 do
                ()

            taskTemp <- [||]

    0
