const firstPython = (req, res) => {
  try {
    var dataToSend
    const python = spawn('python', ['https://github.com/travelwoman/recommender/blob/main/season.py'])
    // collect data from script
    python.stdout.on('data', function (data) {
      console.log('Pipe data from python script ...')
      dataToSend = data.toString()
    })
    python.on('close', (code) => {
      console.log(`child process close all stdio with code ${code}`)
      // send data to browser
      res.send(dataToSend)
    })
  } catch (error) {
    console.log(error)
    res.status(500)
  }
}
