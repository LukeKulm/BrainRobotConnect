let state = "rest";
export default function handler(req, res) {
    if (req.method === 'POST') {
        let x = req.body;
        state = x.data
        res.status(200).json({ message: x })
    } else {
        res.status(200).json({ message: state })
    }
  }